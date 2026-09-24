def test_first(db_session):
    assert db_session["status"] == "connected"


def test_second(db_session):
    assert db_session["user_id"] == 42