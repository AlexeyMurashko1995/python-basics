import pytest
from math_utils import is_even


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
])
def test_is_even(number, expected):
    assert is_even(number) == expected