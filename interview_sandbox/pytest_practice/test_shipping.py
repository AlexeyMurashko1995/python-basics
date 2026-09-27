from shipping import calculate_shipping


def test_calculate_1(mocker):
    mocker.patch("shipping.get_distance", return_value=100)
    assert calculate_shipping(1, 12) == 1200


def test_calculate_2(mocker):
    mocker.patch("shipping.get_distance", return_value=1)
    assert calculate_shipping(2, 432) == 432