async def get_discount(user_id: int) -> float:
    return 10


async def get_final_price(user_id: int, amount) -> float:
    discount = await get_discount(user_id)
    return amount - (discount * amount / 100)