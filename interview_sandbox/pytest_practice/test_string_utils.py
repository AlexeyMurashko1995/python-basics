import pytest
from string_utils import reverse_string


@pytest.mark.parametrize("text, expected", [
    ("python", "nohtyp"),
    ("", ""),
    ("radar", "radar"),
])
def test_reverse(text, expected):
    assert reverse_string(text) == expected


def test_reverse_failure():
    with pytest.raises(TypeError):
        reverse_string(123)