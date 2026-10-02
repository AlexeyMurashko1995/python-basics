async def get_discount(user_id: int) -> float:
    return 0.0


async def calculate_final_price(price: float, user_id: int) -> float:
    discount = await get_discount(user_id)
    return price * (1 - discount)