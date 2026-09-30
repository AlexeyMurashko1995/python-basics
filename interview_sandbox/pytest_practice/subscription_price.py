async def calculate_subscription_price(price: float, user_id: int, get_level) -> float:
    level = await get_level(user_id)
    if level == "PRO":
        return price / 2
    return price