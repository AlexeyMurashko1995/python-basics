import pytest


@pytest.fixture(scope="module")
def db_session():
    print("\n[SETUP] Opening database connection...")
    yield {"status": "connected", "user_id": 42}
    print("\n[TEARDOWN] Closing database connection...")