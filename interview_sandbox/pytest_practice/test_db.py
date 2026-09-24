def test_db_connection(db_session):
    assert db_session["status"] == "connected"