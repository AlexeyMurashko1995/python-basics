async def calculate_delivery(weight: float, user_id: int, get_user_tier) -> float:
    tier = await get_user_tier(user_id)
    if tier == "VIP":
        return weight * 5
    return weight * 10
