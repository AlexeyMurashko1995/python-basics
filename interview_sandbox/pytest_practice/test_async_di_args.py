import pytest
import pytest_asyncio
from async_di_args import get_discounted_price


@pytest.mark.asyncio
async def test_discounted_price(mocker):
    mock_discount = mocker.AsyncMock(return_value=15)
    assert await get_discounted_price(100, 42, mock_discount) == 85
    mock_discount.assert_called_once_with(42)