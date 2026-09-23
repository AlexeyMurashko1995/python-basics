import pytest

@pytest.fixture
def user_data():
    return {"name": "Alexey", "role": "admin"}