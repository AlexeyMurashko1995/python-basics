import pytest
from string_utils import reverse_string

def test_reverse_success():
    assert reverse_string("python") == "nohtyp"


def test_reverse_failure():
    with pytest.raises(TypeError):
        reverse_string(123)