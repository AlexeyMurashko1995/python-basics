import pytest
from discount_calculator import apply_discount


@pytest.mark.parametrize("price, discount, expected", [
    (10, 0, 10),
    (10, 20, 8),
    (10, 100, 0),
])
def test_discount_calculator_params(price, discount, expected):
    assert apply_discount(price, discount) == expected


def test_calculator_fixture(base_price):
    assert apply_discount(base_price, 10) == 90.0


def test_calculator_failure():
    with pytest.raises(ValueError):
        apply_discount(10, -1)