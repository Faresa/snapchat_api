"""
Main script to automate Snapchat Ads campaign management based on ROAS performance.

Dependencies:
- snapchat_api.py: For API interactions
- campaign_management.py: For campaign management logic
- utils.py: For utility functions
"""

from snapchat_api import SnapchatAdsAPI
from campaign_management import manage_campaigns
from utils import get_last_30_days

def get_user_input():
    """
    Gather user configuration via console input with error handling.

    This function ensures that both the access token and account ID are provided
    before continuing, stripping any leading or trailing spaces from the input.
    """
    while True:
        access_token = input("Please enter your Snapchat Ads API Access Token: ").strip()
        if access_token:
            break
        else:
            print("Access Token cannot be empty. Please try again.")

    while True:
        account_id = input("Please enter your Snapchat Account ID: ").strip()
        if account_id:
            break
        else:
            print("Account ID cannot be empty. Please try again.")

    return access_token, account_id

def main():
    """
    Main execution function that:
    - Collects user input for API authentication
    - Initializes the API object
    - Fetches campaign data for the last 30 days
    - Manages campaigns based on ROAS
    """
    ACCESS_TOKEN, ACCOUNT_ID = get_user_input()

    api = SnapchatAdsAPI(ACCESS_TOKEN, ACCOUNT_ID)
    start_date, end_date = get_last_30_days()
    
    print(f"Fetching stats from {start_date} to {end_date}")
    manage_campaigns(api, start_date, end_date)

if __name__ == "__main__":
    main()
