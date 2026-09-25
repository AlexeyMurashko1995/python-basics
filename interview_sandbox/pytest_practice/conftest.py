import pytest


@pytest.fixture
def sample_users():
    return [
        {"name": "Alice", "is_active": True},
        {"name": "Bob", "is_active": False},
        {"name": "Charlie", "is_active": True},
    ]