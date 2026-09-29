async def calculate_user_bonus(score: int, user_id: int, get_coeff):
    coeff = await get_coeff(user_id)
    return score * coeff