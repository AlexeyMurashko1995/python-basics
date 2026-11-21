import httpx


def create_payout(recipient_iban: str, amount: float, currency: str) -> dict:
    payload = {"iban": recipient_iban, "amount": amount, "currency": currency}
    url = "https://postman-echo.com/post"
    timeout = 5.0
    response = httpx.post(url=url, json=payload, timeout=timeout)
    return response.json()


if __name__ == "__main__":
    print(create_payout(recipient_iban="123ad", amount=51.2, currency="EUR"))