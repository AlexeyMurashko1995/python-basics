import pytest


@pytest.fixture
def user_data():
    return {"name": "Alexey", "role": "admin"}


def test_user_role(user_data):
    assert user_data["role"] == "admin"


def test_user_name(user_data):
    assert user_data["name"] == "Alexey"