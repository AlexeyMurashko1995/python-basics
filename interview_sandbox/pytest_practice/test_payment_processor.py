from payment_processor import is_order_paid

def test_is_order_paid_success(mocker):
    mocker.patch("payment_processor.get_payment_status", return_value="PAID")
    assert is_order_paid("pay_123")


def test_is_order_paid_pending(mocker):
    mocker.patch("payment_processor.get_payment_status", return_value="PENDING")
    assert not is_order_paid("pay_123")