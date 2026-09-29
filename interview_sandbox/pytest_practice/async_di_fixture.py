async def get_discounted_price(price: float, user_id: int, discount_func):
    discount = await discount_func(user_id)
    return price - (price * discount / 100)