from currency import convert_usd_to_eur

def test_result_convert_1(mocker):
    mocker.patch("currency.get_exchange_rate", return_value=1.05)
    assert convert_usd_to_eur(100) == 105


def test_result_convert_2(mocker):
    mocker.patch("currency.get_exchange_rate", return_value=0.9)
    assert convert_usd_to_eur(100) == 90