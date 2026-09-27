def get_coeff(region_id: int) -> float:
    return 5


def get_subscription_price(region_id: int, full_price: float) -> float:
    coeff = get_coeff(region_id)
    return full_price - (coeff * full_price / 100)