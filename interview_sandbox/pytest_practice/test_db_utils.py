def test_db_is_connected(db_session):
    assert db_session.is_connected == True


def test_db_remains_connected(db_session):
    assert db_session.is_connected == True