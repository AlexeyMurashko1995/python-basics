import pytest
from async_cargo import get_cargo_final_price


@pytest.mark.parametrize("coeff, expected", [
    ("LOCAL", 100),
    ("EU", 150),
    ("GB", 200)
])
@pytest.mark.asyncio
async def test_cargo_price(coeff, expected, mocker):
    mocker_coeff = mocker.AsyncMock(return_value=coeff)
    assert await get_cargo_final_price(10, 1, mocker_coeff) == expected
    mocker_coeff.assert_called_once_with(1)