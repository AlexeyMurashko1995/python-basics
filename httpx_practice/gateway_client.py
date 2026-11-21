import httpx


def check_transaction(tx_id: str, api_key: str) -> dict:
    url = "https://postman-echo.com/get"
    params = {"transaction_id": tx_id}
    headers = {"X-API-Key": api_key}
    timeout = 5.0
    response = httpx.get(url=url, params=params, headers=headers, timeout=timeout)
    return response.json()