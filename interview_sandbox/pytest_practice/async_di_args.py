async def get_discounted_price(price: float, user_id: int, discount_func) -> float:
    discount = await discount_func(user_id)
    return price - (discount * price / 100)