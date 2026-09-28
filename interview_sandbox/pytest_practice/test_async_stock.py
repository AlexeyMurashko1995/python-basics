import pytest
import pytest_asyncio
from async_stock import get_product_price


@pytest.mark.asyncio
async def test_option_success(mocker):
    mocker.patch("async_stock.get_product_in_stock",new_callable=mocker.AsyncMock, return_value=True)
    assert await get_product_price(1) == 20


@pytest.mark.asyncio
async def test_option_failure(mocker):
    with pytest.raises(ValueError):
        mocker.patch("async_stock.get_product_in_stock", new_callable=mocker.AsyncMock, return_value=False)
        await get_product_price(1)