def check_status(score: int) -> str:
    if score >= 80:
        return "passed"
    elif score >= 50:
        return "retry"
    return "failed"