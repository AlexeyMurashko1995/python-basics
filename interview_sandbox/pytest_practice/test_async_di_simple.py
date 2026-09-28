import pytest
import pytest_asyncio
from async_di_simple import get_total_price


@pytest.mark.asyncio
async def test_total_price(mocker):
    mock_discount = mocker.AsyncMock(return_value=10)
    assert await get_total_price(100, mock_discount) == 90