import pytest
from status_checker import check_status


@pytest.mark.parametrize("score, expected", [
    (90, "passed"),
    (60, "retry"),
    (30, "failed"),
])
def test_check_status(score, expected):
    assert check_status(score) == expected