import pytest
from user_utils import filter_active_users

def test_filter_active_users(sample_users):
    result = filter_active_users(sample_users)
    assert result == ["Alice", "Charlie"]