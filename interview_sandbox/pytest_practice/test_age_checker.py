import pytest
from age_checker import check_age


def test_age_success():
    assert check_age(20) == True


def test_age_failure():
    with pytest.raises(ValueError):
        check_age(121)