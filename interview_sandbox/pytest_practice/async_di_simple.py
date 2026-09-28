async def get_total_price(price: float, discount_func) -> float:
    discount = await discount_func()
    return price - (price * discount / 100)