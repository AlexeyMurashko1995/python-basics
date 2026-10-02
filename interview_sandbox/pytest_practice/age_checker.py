async def check_age(age: int) -> str:
    if age < 18:
        raise ValueError("Too young")
    elif age > 100:
        raise ValueError("Too old")
    return "OK"
