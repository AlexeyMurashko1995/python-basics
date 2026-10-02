import pytest
from exchange_rate import convert_currency


@pytest.mark.asyncio
async def test_convert_currency(mocker):
    convert_mocker = mocker.patch("exchange_rate.get_exchange_rate", return_value=75)
    assert await convert_currency(100, "USD") == 7500
    convert_mocker.assert_called_once_with("USD")