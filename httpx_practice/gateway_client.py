import httpx


def fetch_echo(query: str) -> dict:
    url = "https://postman-echo.com/get"
    params = {"q": query}
    timeout = 5.0
    response = httpx.get(url=url, params=params, timeout=timeout)
    return response.json()


def send_echo_data(message: str, amount: float) -> dict:
    url = "https://postman-echo.com/post"
    payload = {"message": message, "amount": amount}
    timeout = 5.0
    response = httpx.post(url=url, json=payload, timeout=timeout)
    return response.json()