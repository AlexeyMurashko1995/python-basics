import pytest


@pytest.mark.asyncio
async def test_health_check(get_client):
    response = await get_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_get_version(get_client):
    response = await get_client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}


@pytest.mark.asyncio
async def test_get_status(get_client):
    response = await get_client.get("/api/v1/status")
    assert response.status_code == 200
    assert response.json() == {"service": "auth_service", "online": True}