import pytest
from async_cashback import get_cashback


@pytest.mark.parametrize("status, expected", [
    ("PLATINUM", 20),
    ("GOLD", 10),
    ("BRONZE", 2)
])

@pytest.mark.asyncio
async def test_cashback(status, expected, mocker):
    mocker_coeff = mocker.AsyncMock(return_value=status)
    assert await get_cashback(200, 42, mocker_coeff) == expected
    mocker_coeff.assert_called_once_with(42)