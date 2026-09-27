import pytest
import pytest_asyncio
from async_discount import get_final_price


@pytest.mark.asyncio
async def test_option_1():
    assert await get_final_price(1, 100) == 90


@pytest.mark.asyncio
async def test_option_2(mocker):
    mocker.patch("async_discount.get_discount", new_callable=mocker.AsyncMock, return_value=20)
    assert await get_final_price(1, 100) == 80