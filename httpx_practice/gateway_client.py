import httpx


def send_authorized_payout(api_key: str, payload: dict) -> dict:
    base_url = "https://postman-echo.com"
    headers = {"X-API-Key": api_key}
    timeout = 5.0
    with httpx.Client(base_url=base_url, headers=headers, timeout=timeout) as client:
        try:
            response = client.post("/post", json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            return {"error": exc.response.status_code}


if __name__ == "__main__":
    print(send_authorized_payout(api_key="123.123.23.2", payload={"amount": 12}))