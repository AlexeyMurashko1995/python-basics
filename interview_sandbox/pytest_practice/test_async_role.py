import pytest
from async_role import get_discount


@pytest.mark.parametrize("role, expected", [
    ("ADMIN", 70),
    ("USER", 90),
    ("GUEST", 100)
])
@pytest.mark.asyncio
async def test_get_discount(mocker, role, expected):
    mock_get_role = mocker.AsyncMock(return_value=role)
    assert await get_discount(100, 1, mock_get_role) == expected
    mock_get_role.assert_called_once_with(1)