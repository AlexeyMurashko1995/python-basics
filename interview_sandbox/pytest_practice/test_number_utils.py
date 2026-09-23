import pytest
from number_utils import is_positive


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (-3, False),
    (0, False),
])
def test_is_positive(number, expected):
    assert is_positive(number) == expected