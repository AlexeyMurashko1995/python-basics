import pytest
from async_tax import calculate_total_with_tax


@pytest.mark.asyncio
async def test_calculate_total(mocker):
    mock_tax = mocker.AsyncMock(return_value=10)
    assert await calculate_total_with_tax(100, "PL", mock_tax) == 110
    mock_tax.assert_called_once_with("PL")