import httpx


def check_transaction(tx_id: str, api_key: str) -> dict:
    url = "https://postman-echo.com/get"
    params = {"transaction_id": tx_id}
    headers = {"X-API-Key": api_key}
    timeout = 5.0
    response = httpx.get(url=url, params=params, headers=headers, timeout=timeout)
    return response.json()


def diagnose_status(status_code: int) -> str:
    url = f"https://postman-echo.com/status/{status_code}"
    try:
        response = httpx.get(url=url, timeout=5.0)
    except httpx.RequestError as exc:
        return f"Error: {exc}"

    if response.status_code == 200:
        return "200 OK: Request succeeded"
    if response.status_code == 401:
        return "401 Unauthorized: Check API key"
    if response.status_code == 403:
        return "403 Forbidden: IP not in whitelist"
    if response.status_code == 500:
        return "500 Server Error: Downstream backend failed"
    return f"Unhandled status: {response.status_code}"


if __name__ == "__main__":
    print(check_transaction(tx_id="123af", api_key="123.123.1231.2"))
    print(diagnose_status(status_code=200))
    print(diagnose_status(status_code=403))
    print(diagnose_status(status_code=500))