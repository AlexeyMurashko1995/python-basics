import pytest
import pytest_asyncio
from async_payment import get_payment_confirmation


@pytest.mark.asyncio
async def test_option_failure(mocker):
    mocker.patch("async_payment.get_status", new_callable=mocker.AsyncMock, return_value=False)
    with pytest.raises(ValueError):
        await get_payment_confirmation(1)


@pytest.mark.asyncio
async def test_option_success(mocker):
    mocker.patch("async_payment.get_status", new_callable=mocker.AsyncMock, return_value=True)
    assert await get_payment_confirmation(1)