import pytest
from async_discount import apply_user_discount


@pytest.mark.asyncio
async def test_user_discount(mocker):
    mocker_discount = mocker.AsyncMock(return_value=15)
    assert await apply_user_discount(100, 1, mocker_discount) == 85
    mocker_discount.assert_called_once_with(1)