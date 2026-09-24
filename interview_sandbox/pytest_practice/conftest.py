import pytest


@pytest.fixture
def user_data():
    return {"name": "Ivan", "role": "backend engineer"}