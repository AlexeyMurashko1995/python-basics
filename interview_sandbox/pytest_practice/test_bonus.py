from bonus import get_final_bonus


def test_option_1(mocker):
    mocker.patch("bonus.get_loyalty_level", return_value="gold")
    assert get_final_bonus(1, 100) == 10


def test_option_2(mocker):
    mocker.patch("bonus.get_loyalty_level", return_value="standard")
    assert get_final_bonus(1, 100) == 0