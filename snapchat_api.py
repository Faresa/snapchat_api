"""
Module for automating interactions with the Snapchat Ads API.

This module provides classes and methods to:
- Fetch campaign statistics
- Pause campaigns
"""

import requests
from datetime import datetime

class SnapchatAdsAPI:
    def __init__(self, access_token, account_id):
        """
        Initialize the Snapchat Ads API automation object.

        :param access_token: Bearer token for API authentication
        :param account_id: The Snapchat Ad Account ID
        """
        self.base_url = "https://adsapi.snapchat.com/v1/adaccounts/"
        self.access_token = access_token
        self.account_id = account_id
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

    def get_campaign_stats(self, start_date, end_date):
        """
        Fetch campaign performance statistics for a given date range.

        :param start_date: Start date for stats (datetime object)
        :param end_date: End date for stats (datetime object)
        :return: JSON response from API or None if an error occurs
        """
        params = {
            "granularity": "DAY",
            "start_time": start_date.isoformat(),
            "end_time": end_date.isoformat(),
            "fields": "spend,conversion_purchases_value",
            "breakdown": "campaign"
        }
        url = f"{self.base_url}{self.account_id}/stats"
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching campaign stats: {e}")
            return None

    def pause_campaign(self, campaign_id):
        """
        Pause a specific campaign.

        :param campaign_id: ID of the campaign to pause
        :return: Boolean indicating if the pause was successful
        """
        url = f"{self.base_url}{self.account_id}/campaigns/{campaign_id}/pause"
        try:
            response = requests.post(url, headers=self.headers, timeout=5)
            response.raise_for_status()
            print(f"Campaign {campaign_id} paused successfully.")
            return True
        except requests.RequestException as e:
            print(f"Error pausing campaign {campaign_id}: {e}")
            return False
