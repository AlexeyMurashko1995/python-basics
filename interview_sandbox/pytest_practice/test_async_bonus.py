import pytest
from async_bonus import calculate_user_bonus


@pytest.mark.asyncio
async def test_user_bonus(mocker):
    mock_bonus = mocker.AsyncMock(return_value=10)
    assert await calculate_user_bonus(100, 1, mock_bonus) == 1000
    mock_bonus.assert_called_once_with(1)