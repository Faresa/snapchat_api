import pytest
from unittest.mock import Mock, patch
from campaign_management import manage_campaigns
from snapchat_api import SnapchatAdsAPI
from utils import calculate_roas
from datetime import datetime

def setup_test_api():
    return SnapchatAdsAPI("mock_token", "mock_account_id")

def test_manage_campaigns_pause():
    api = setup_test_api()
    api.get_campaign_stats = Mock(return_value={
        "daily_stats": [
            {"campaign": {"id": "test_id"}, "daily_stat": {"spend": 100, "conversion_purchases_value": 50}}
        ]
    })
    api.pause_campaign = Mock(return_value=True)
    
    with patch('builtins.print') as mock_print:
        manage_campaigns(api, datetime(2025, 1, 1), datetime(2025, 1, 31))
        mock_print.assert_any_call("Campaign test_id has ROAS: 0.50")
        mock_print.assert_any_call("Successfully paused campaign test_id due to low ROAS of 0.50")

def test_manage_campaigns_no_pause():
    api = setup_test_api()
    api.get_campaign_stats = Mock(return_value={
        "daily_stats": [
            {"campaign": {"id": "test_id"}, "daily_stat": {"spend": 100, "conversion_purchases_value": 200}}
        ]
    })
    api.pause_campaign = Mock(return_value=True)
    
    with patch('builtins.print') as mock_print:
        manage_campaigns(api, datetime(2025, 1, 1), datetime(2025, 1, 31))
        mock_print.assert_called_once_with("Campaign test_id has ROAS: 2.00")

def test_manage_campaigns_pause_fails():
    api = setup_test_api()
    api.get_campaign_stats = Mock(return_value={
        "daily_stats": [
            {"campaign": {"id": "test_id"}, "daily_stat": {"spend": 100, "conversion_purchases_value": 50}}
        ]
    })
    api.pause_campaign = Mock(return_value=False)
    
    with patch('builtins.print') as mock_print:
        manage_campaigns(api, datetime(2025, 1, 1), datetime(2025, 1, 31))
        mock_print.assert_any_call("Failed to pause campaign test_id, ROAS was 0.50")
