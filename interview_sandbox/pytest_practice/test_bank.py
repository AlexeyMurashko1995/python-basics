from bank import get_transfer

def test_transfer_1(mocker):
    mocker.patch("bank.get_balance", return_value=500)
    assert get_transfer(1, 200) == True


def test_transfer_2(mocker):
    mocker.patch("bank.get_balance", return_value=100)
    assert get_transfer(1, 200) == False