def divide(a: int, b: int):
    return a / b


def check_age(age: int):
    if age >= 18:
        return "Adult"
    elif age < 0:
        raise ValueError("Invalid error")


def multiply(a: int, b: int):
    return a * b