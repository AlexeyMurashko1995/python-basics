async def calculate_cashback(amount: float, user_id: int, cashback_func) -> float:
    rate = await cashback_func(user_id)
    return amount * rate / 100