async def make_payment(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Amount must be positive")
    elif amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount