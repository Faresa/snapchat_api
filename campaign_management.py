"""
Module for managing Snapchat Ads campaigns based on ROAS.

This module will:
- Calculate ROAS for campaigns
- Decide if campaigns should be paused
- Execute campaign pausing
"""

from snapchat_api import SnapchatAdsAPI
from utils import calculate_roas

def manage_campaigns(api, start_date, end_date):
    """
    Manage campaigns based on their ROAS.

    :param api: SnapchatAdsAPI instance
    :param start_date: Start date for stats review
    :param end_date: End date for stats review
    """
    stats = api.get_campaign_stats(start_date, end_date)
    if stats:
        for campaign in stats.get('daily_stats', []):
            if 'campaign' in campaign and 'daily_stat' in campaign:
                campaign_data = campaign['campaign']
                daily_stat = campaign['daily_stat']
                roas = calculate_roas(daily_stat.get('spend', 0), daily_stat.get('conversion_purchases_value', 0))
                
                print(f"Campaign {campaign_data['id']} has ROAS: {roas:.2f}")
                if roas < 1:  
                    if api.pause_campaign(campaign_data['id']):
                        print(f"Successfully paused campaign {campaign_data['id']} due to low ROAS of {roas:.2f}")
                    else:
                        print(f"Failed to pause campaign {campaign_data['id']}, ROAS was {roas:.2f}")
            else:
                print(f"Campaign data incomplete for {campaign}")
    else:
        print("No data retrieved or an error occurred while fetching stats.")
