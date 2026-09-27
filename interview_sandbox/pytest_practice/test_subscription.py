from subscription import get_subscription_price


def test_option_1(mocker):
    mocker.patch("subscription.get_coeff", return_value=10)
    assert get_subscription_price(1, 200) == 180


def test_option_2(mocker):
    mocker.patch("subscription.get_coeff", return_value=0)
    assert get_subscription_price(1, 200) == 200