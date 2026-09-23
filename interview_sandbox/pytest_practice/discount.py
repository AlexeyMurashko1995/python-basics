def get_discount(price: float, discount: float):
    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount")
    return price - (price * discount / 100)