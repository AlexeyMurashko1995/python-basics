import pytest
from async_payment import make_payment


@pytest.mark.asyncio
async def test_payment_success():
    assert await make_payment(100, 50) == 50


@pytest.mark.asyncio
async def test_payment_failure_1():
    with pytest.raises(ValueError, match="Insufficient funds"):
        await make_payment(50, 100)


@pytest.mark.asyncio
async def test_payment_failure_2():
    with pytest.raises(ValueError, match="Amount must be positive"):
        await make_payment(50, -2)