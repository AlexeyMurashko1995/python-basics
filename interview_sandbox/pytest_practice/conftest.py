import pytest
from db_utils import DatabaseConnection


@pytest.fixture(scope="module")
def db_session():
    db = DatabaseConnection()
    db.connect()
    yield db
    db.disconnect()