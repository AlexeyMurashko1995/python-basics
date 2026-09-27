def get_discount(user_id: int) -> int:
    return 10


def get_final_price(user_id: int, amount: float) -> float:
    discount = get_discount(user_id)
    return amount - (discount * amount / 100)
