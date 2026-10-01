import pytest
from shipping import calculate_shipping_cost


@pytest.mark.parametrize("status, expected", [
    ("GOLD", 50),
    ("SILVER", 80),
    ("STONE", 100)
])
@pytest.mark.asyncio
async def test_calculate_shipping_cost(status, expected, mocker):
    mocker_status = mocker.AsyncMock(return_value=status)
    assert await calculate_shipping_cost(10, 42, mocker_status) == expected
    mocker_status.assert_called_once_with(42)