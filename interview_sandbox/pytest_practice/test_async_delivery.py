import pytest
from async_delivery import calculate_delivery


@pytest.fixture
def mock_vip_tier(mocker):
    return mocker.AsyncMock(return_value="VIP")


@pytest.mark.asyncio
async def test_calculator_delivery(mock_vip_tier):
    assert await calculate_delivery(5, 42, mock_vip_tier) == 25
    mock_vip_tier.assert_called_once_with(42)