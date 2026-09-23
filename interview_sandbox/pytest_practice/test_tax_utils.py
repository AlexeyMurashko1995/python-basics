import pytest
from tax_utils import calculate_tax


@pytest.mark.parametrize("amount, rate, expected", [
    (100.0, 20.0, 20.0),
    (200.0, 0.0, 0.0),
    (50.0, 10.0, 5.0),
])
def test_tax(amount, rate, expected):
    assert calculate_tax(amount, rate) == expected