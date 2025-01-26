import pytest
from unittest.mock import Mock, patch
from snapchat_api import SnapchatAdsAPI
from datetime import datetime

def setup_test_api():
    return SnapchatAdsAPI("mock_token", "mock_account_id")

def test_get_campaign_stats_success():
    api = setup_test_api()
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {"daily_stats": [{"campaign": {"id": "test_id"}, "daily_stat": {"spend": 100, "conversion_purchases_value": 50}}]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        result = api.get_campaign_stats(datetime(2025, 1, 1), datetime(2025, 1, 31))
        assert result is not None
        assert len(result["daily_stats"]) == 1

def test_get_campaign_stats_failure():
    api = setup_test_api()
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("API error")
        result = api.get_campaign_stats(datetime(2025, 1, 1), datetime(2025, 1, 31))
        assert result is None  # Expect None due to error

def test_pause_campaign_success():
    api = setup_test_api()
    with patch('requests.post') as mock_post:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        result = api.pause_campaign("test_id")
        assert result

def test_pause_campaign_failure():
    api = setup_test_api()
    with patch('requests.post') as mock_post:
        mock_post.side_effect = Exception("Failed to pause")
        result = api.pause_campaign("test_id")
        assert not result  # Expect False due to exception
