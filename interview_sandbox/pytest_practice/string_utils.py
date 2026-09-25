def reverse_string(text: str) -> str:
    if type(text) != str:
        raise TypeError
    return text[::-1]