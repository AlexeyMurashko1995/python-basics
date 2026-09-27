from discount_service import get_final_price


def test_option_1(mocker):
    mocker.patch("discount_service.get_discount", return_value=20)
    assert get_final_price(1, 100) == 80


def test_option_2(mocker):
    mocker.patch("discount_service.get_discount", return_value=0)
    assert get_final_price(1, 100) == 100