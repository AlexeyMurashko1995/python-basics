import httpx


BASE_URL = "https://postman-echo.com"
DEFAULT_TIMEOUT = 5.0


def get_status_code() -> int:
    response = httpx.get(url=f"{BASE_URL}/get", timeout=DEFAULT_TIMEOUT)
    return response.status_code


def get_json(query: str) -> dict:
    params = {"q": query}
    response = httpx.get(
        url=f"{BASE_URL}/get",
        timeout=DEFAULT_TIMEOUT,
        params=params,
    )
    return response.json()


def post_message(message: str) -> dict:
    payload = {"message": message}
    response = httpx.post(
        url=f"{BASE_URL}/post",
        timeout=DEFAULT_TIMEOUT,
        json=payload,
    )
    return response.json()


if __name__ == "__main__":
    print(get_status_code())
    print(get_json(query="test"))
    print(post_message(message="hello"))