import pytest
import pytest_asyncio
from async_di_fixture import get_discounted_price


@pytest.fixture
def mock_discount_service(mocker):
    return mocker.AsyncMock(return_value=20)


@pytest.mark.asyncio
async def test_discounted_price(mock_discount_service):
    assert await get_discounted_price(100, 1, mock_discount_service) == 80
    mock_discount_service.assert_called_once_with(1)