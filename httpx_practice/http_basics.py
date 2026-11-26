import httpx


def get_status_code() -> int:
    url = "https://postman-echo.com/get"
    timeout = 5.0
    response = httpx.get(url=url, timeout=timeout)
    return response.status_code


if __name__ == "__main__":
    print(get_status_code())