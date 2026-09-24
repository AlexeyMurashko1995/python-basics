import pytest
from calculator import divide


def test_divide_success():
    assert divide(10, 2) == 5


def test_divide_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)