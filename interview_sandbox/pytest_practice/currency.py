def get_exchange_rate() -> float:
    return 1.0


def convert_usd_to_eur(usd_amount: int) -> float:
    exchange_result = get_exchange_rate()
    return usd_amount * exchange_result