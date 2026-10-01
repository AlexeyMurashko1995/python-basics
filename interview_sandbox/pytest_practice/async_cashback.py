async def get_cashback(amount: float, user_id: int, get_coeff):
    coeff = await get_coeff(user_id)
    if coeff == "PLATINUM":
        return amount * 0.10
    elif coeff == "GOLD":
        return amount * 0.05
    else:
        return amount * 0.01