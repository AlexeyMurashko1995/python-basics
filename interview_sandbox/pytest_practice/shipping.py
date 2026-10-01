async def calculate_shipping_cost(weight: float, user_id: int, get_status):
    status = await get_status(user_id)
    if status == "GOLD":
        return weight * 5
    elif status == "SILVER":
        return weight * 8
    else:
        return weight * 10