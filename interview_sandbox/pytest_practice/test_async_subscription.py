import pytest
from async_subscription import calculate_subscription_price


@pytest.fixture
def mocker_level(mocker):
    return mocker.AsyncMock(return_value="PRO")


@pytest.mark.asyncio
async def test_calculate_price(mocker_level):
    assert await calculate_subscription_price(100, 12, mocker_level) == 50
    mocker_level.assert_called_once_with(12)