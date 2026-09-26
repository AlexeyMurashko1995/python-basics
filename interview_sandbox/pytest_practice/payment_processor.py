def get_payment_status(payment_id: str) -> str:
    return "PENDING..."


def is_order_paid(payment_id: str) -> bool:
    result = get_payment_status(payment_id=payment_id)
    if result == "PAID":
        return True
    return False