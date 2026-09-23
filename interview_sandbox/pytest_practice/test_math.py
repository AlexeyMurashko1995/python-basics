import pytest
from math_utils import divide, check_age, multiply


def test_divide_success():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_check_success():
    assert check_age(20) == "Adult"


def test_age_invalid():
    with pytest.raises(ValueError):
        check_age(-2)


def test_multiply_connect():
    assert multiply(2, 5) == 10