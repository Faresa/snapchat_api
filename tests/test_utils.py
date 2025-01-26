import pytest
from utils import get_last_30_days, calculate_roas
from datetime import datetime, timedelta

def test_get_last_30_days():
    start_date, end_date = get_last_30_days()
    assert (end_date - start_date).days == 29  # Should be 30 days minus 1 day for today

def test_calculate_roas():
    assert calculate_roas(100, 100) == 1.0
    assert calculate_roas(100, 0) == 0.0
    assert calculate_roas(0, 100) == float('inf')  # Handle division by zero
    assert calculate_roas(50, 100) == 2.0

def test_calculate_roas_zero_spend():
    assert calculate_roas(0, 50) == float('inf')
