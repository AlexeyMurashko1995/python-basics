def get_discount(code: str) -> int:
    if code == "SUMMER20":
        return 10
    return 0


def get_final_price(amount: int, code: str) -> float:
    discount = get_discount(code)
    return amount - (discount * amount / 100)