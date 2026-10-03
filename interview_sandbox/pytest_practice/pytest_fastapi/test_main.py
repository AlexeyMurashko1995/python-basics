import pytest


@pytest.mark.asyncio
async def test_health_check(get_client):
    response = await get_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}