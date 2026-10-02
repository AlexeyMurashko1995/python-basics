async def get_exchange_rate(currency: str) -> float:
    return 1.0


async def convert_currency(amount: float, currency: str) -> float:
    rate = await get_exchange_rate(currency)
    return rate * amount