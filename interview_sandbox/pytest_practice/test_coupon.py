from coupon import get_final_price


def test_coupon_1(mocker):
    mocker.patch("coupon.get_discount", return_value=20)
    assert get_final_price(1000, "SUMMER20") == 800


def test_coupon_2(mocker):
    mocker.patch("coupon.get_discount", return_value=0)
    assert get_final_price(1000, "INVALID") == 1000