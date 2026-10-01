async def apply_user_discount(price: float, user_id: int, fetch_discount) -> float:
    discount = await fetch_discount(user_id)
    return price - discount