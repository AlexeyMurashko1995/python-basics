import pytest


@pytest.mark.asyncio
async def test_get_dict(get_client):
    response = await get_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_add_items(get_client):
    response = await get_client.post(url="/items", json={"name": "Phone", "price": 12})
    assert response.status_code == 200
    assert response.json() == {"status": "created", "data": {"name": "Phone", "price": 12}}
