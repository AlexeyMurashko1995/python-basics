async def get_discount(amount: float, user_id: int, get_role) -> float:
    role = await get_role(user_id)
    if role == "ADMIN":
        return amount - (30 * amount / 100)
    elif role == "USER":
        return amount - (10 * amount / 100)
    else:
        return amount