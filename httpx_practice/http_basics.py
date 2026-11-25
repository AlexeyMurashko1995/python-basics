import httpx


BASE_URL = "https://postman-echo.com"
DEFAULT_TIMEOUT = 5.0


def get_request() -> int:
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


def post_request(body: str) -> dict:
    payload = {"message": body}
    response = httpx.post(
        url=f"{BASE_URL}/post",
        timeout=DEFAULT_TIMEOUT,
        json=payload,
    )
    return response.json()


def get_with_headers(api_key: str) -> dict:
    headers = {"X-API-Key": api_key}
    response = httpx.get(
        url=f"{BASE_URL}/get",
        timeout=DEFAULT_TIMEOUT,
        headers=headers,
    )
    return response.json()


if __name__ == "__main__":
    print(get_request())
    print(get_json(query="123"))
    print(post_request(body="alex"))
    print(get_with_headers(api_key="test-key-123"))