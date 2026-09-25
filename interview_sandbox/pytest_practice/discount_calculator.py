def apply_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 100:
        raise ValueError
    return price - (price * (discount / 100))