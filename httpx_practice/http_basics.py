import httpx


def get_request() -> int:
    url = "https://postman-echo.com/get"
    timeout = 5.0
    response = httpx.get(url=url, timeout=timeout)
    return response.status_code


def get_json(query: str) -> dict:
    url = "https://postman-echo.com/get"
    timeout = 5.0
    payload = {"q": query}
    response = httpx.get(url=url, timeout=timeout, params=payload)
    return response.json()


if __name__ == "__main__":
    print(get_request())
    print(get_json(query="123"))