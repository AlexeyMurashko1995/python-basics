def tax_status(wages: float) -> float:
    if wages > 100000:
        return 0.30
    elif 50000 <= wages <= 100000:
        return 0.20
    return 0.10