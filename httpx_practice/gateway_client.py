import httpx


def fetch_echo(query: str) -> dict:
    url = "https://postman-echo.com/get"
    params = {"q": query}
    timeout = 5.0
    response = httpx.get(url=url, params=params, timeout=timeout)
    return response.json()