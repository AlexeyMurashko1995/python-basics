def check_age(age: int) -> bool:
    if age < 0 or age > 120:
        raise ValueError("Invalid age")
    return True