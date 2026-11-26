import httpx


def get_status_code() -> int:
    url = "https://postman-echo.com/get"
    timeout = 5.0
    response = httpx.get(url=url, timeout=timeout)
    return response.status_code


def get_json(query: str) -> dict:
    url = "https://postman-echo.com/get"
    timeout = 5.0
    params = {"q": query}
    response = httpx.get(url=url, timeout=timeout, params=params)
    return response.json()


if __name__ == "__main__":
    print(get_status_code())
    print(get_json(query="test"))