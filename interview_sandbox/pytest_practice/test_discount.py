import pytest
from discount import get_discount


def test_discount_success():
    assert get_discount(100, 10) == 90


def test_discount_fail():
    with pytest.raises(ValueError):
        get_discount(10, -2)