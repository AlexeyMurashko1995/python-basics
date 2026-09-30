def get_discount(price: float) -> float:
    if price < 100:
        return price
    elif 100 <= price < 500:
        return price - (10 * price / 100)
    else:
        return price - (20 * price / 100)