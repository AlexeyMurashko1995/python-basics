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


def check_endpoint_status(status_code: int, api_key: str) -> dict:
    url = f"https://postman-echo.com/status/{status_code}"
    headers = {"X-API-Key": api_key}
    timeout = 5.0
    try:
        response = httpx.get(url=url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return {"status": response.status_code}
    except httpx.HTTPStatusError as exc:
        return {"error": exc.response.status_code}
    except httpx.RequestError:
        return {"error": "network_error"}


if __name__ == "__main__":
    print(fetch_echo(query="123"))
    print(send_echo_data(message="spam", amount=12.2))
    print(check_endpoint_status(status_code=200, api_key="123.123.23.2"))
    print(check_endpoint_status(status_code=401, api_key="123.23.23.1"))