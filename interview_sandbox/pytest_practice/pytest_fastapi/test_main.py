import pytest


@pytest.mark.asyncio
async def test_add_items_success(get_client):
    response = await get_client.post(url="/api/v1/items", json={"title": "Phone", "price": 120.0})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Phone", "price": 120.0}


@pytest.mark.asyncio
async def test_add_items_validation_error(get_client):
    response = await get_client.post(url="/api/v1/items", json={"title":"Phone", "price": "price"})
    assert response.status_code == 422