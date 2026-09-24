import pytest


@pytest.fixture
def db_session():
    print("Opening database connection...")
    yield {"status": "connected", "user_id": 42}
    print("Closing databse connection")