import pytest
from tax_checker import tax_status


@pytest.mark.parametrize("wages, expected", [
    (150000, 0.30),
    (50000, 0.20),
    (20000, 0.10)
])
def test_tax_status(wages, expected):
    assert tax_status(wages) == expected