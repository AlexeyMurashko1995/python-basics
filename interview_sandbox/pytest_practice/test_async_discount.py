import pytest
from async_discount import calculate_final_price


@pytest.mark.asyncio
async def test_final_price(mocker):
    mocker_discount = mocker.patch("async_discount.get_discount", return_value=0.2)
    assert await calculate_final_price(100, 42) == 80
    mocker_discount.assert_called_once_with(42)