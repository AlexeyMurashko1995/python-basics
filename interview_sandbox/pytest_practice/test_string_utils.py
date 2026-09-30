import pytest
from string_utils import get_discount


@pytest.mark.parametrize("number, expected", [
    (50, 50),
    (100, 90),
    (250, 225),
    (500, 400)
])
def test_discount(number, expected):
    assert get_discount(number) == expected