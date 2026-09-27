def get_loyalty_level(user_id: int) -> str:
    return "gold"


def get_final_bonus(user_id: int, amount: float) -> float:
    level = get_loyalty_level(user_id=user_id)
    if level == "gold":
        return amount * 0.1
    return 0