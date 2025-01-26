"""
Utility functions for date calculations and ROAS computation used in automation scripts.
"""

from datetime import datetime, timedelta

def get_last_30_days():
    """
    Get the date range for the last 30 days excluding today.

    :return: Tuple of (start_date, end_date)
    """
    end_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
    start_date = end_date - timedelta(days=29)
    return start_date, end_date

def calculate_roas(spend, conversion_value):
    """
    Calculate Return on Ad Spend (ROAS).

    :param spend: Amount spent on the campaign
    :param conversion_value: Total value from conversions
    :return: ROAS as a float; returns infinity if spend is 0 to avoid division by zero
    """
    if spend == 0:
        return float('inf')  # Avoid division by zero
    return conversion_value / spend
