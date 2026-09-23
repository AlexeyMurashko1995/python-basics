import pytest
from str_utils import is_even_length


@pytest.mark.parametrize("text, expected", [
    ("python", True),
    ("cool", True),
    ("apple", False)
])
def test_even_length(text, expected):
    assert is_even_length(text) == expected