import pytest
from async_cashback import calculate_cashback


@pytest.fixture
def mock_cashback_rate(mocker):
    return mocker.AsyncMock(return_value=5)


@pytest.mark.asyncio
async def test_calculator_rate(mock_cashback_rate):
    assert await calculate_cashback(1000, 101, mock_cashback_rate) == 50
    mock_cashback_rate.assert_called_once_with(101)