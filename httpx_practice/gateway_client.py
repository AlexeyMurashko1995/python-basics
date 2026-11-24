import httpx

BASE_URL = "https://postman-echo.com"
DEFAULT_TIMEOUT = 5.0


def fetch_echo(query: str) -> dict:
    url = f"{BASE_URL}/get"
    params = {"q": query}
    try:
        response = httpx.get(url, params=params, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as exc:
        return {"error": exc.response.status_code}
    except httpx.TimeoutException:
        return {"error": "timeout"}
    except httpx.RequestError:
        return {"error": "network_error"}


def send_echo_data(message: str, amount: float) -> dict:
    url = f"{BASE_URL}/post"
    payload = {"message": message, "amount": amount}
    try:
        response = httpx.post(url, json=payload, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as exc:
        return {"error": exc.response.status_code}
    except httpx.TimeoutException:
        return {"error": "timeout"}
    except httpx.RequestError:
        return {"error": "network_error"}


def check_endpoint_status(status_code: int, api_key: str) -> dict:
    url = f"{BASE_URL}/status/{status_code}"
    headers = {"X-API-Key": api_key}
    try:
        response = httpx.get(url, headers=headers, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        return {"status": response.status_code}
    except httpx.HTTPStatusError as exc:
        return {"error": exc.response.status_code}
    except httpx.TimeoutException:
        return {"error": "timeout"}
    except httpx.RequestError:
        return {"error": "network_error"}


if __name__ == "__main__":
    print(fetch_echo(query="123"))
    print(send_echo_data(message="spam", amount=12.2))
    print(check_endpoint_status(status_code=200, api_key="123.123.23.2"))
    print(check_endpoint_status(status_code=401, api_key="123.23.23.1"))