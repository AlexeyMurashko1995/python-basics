import pytest
import pytest_asyncio
from async_delivery import calculate_delivery_cost


@pytest.mark.asyncio
async def test_get_delivery_cost(mocker):
    mock_cost = mocker.AsyncMock(return_value=15)
    result = await calculate_delivery_cost(100, 15, mock_cost)
    assert result == 115
    mock_cost.assert_called_once_with(15)