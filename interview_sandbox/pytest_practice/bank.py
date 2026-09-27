def get_balance(user_id: int) -> float:
    return 10


def get_transfer(user_id: int, amount: int) -> bool:
    balance = get_balance(user_id)
    return balance >= amount