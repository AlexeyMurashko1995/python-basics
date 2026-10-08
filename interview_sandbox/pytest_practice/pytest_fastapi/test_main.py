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


@pytest.mark.asyncio
async def test_add_category(get_client):
    response = await get_client.post(url="/api/v1/categories", json={"name": "food", "budget_limit": 120})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "food", "budget_limit": 120}


@pytest.mark.asyncio
async def test_get_categories(get_client):
    request = await get_client.post(url="/api/v1/categories", json={"name": "food", "budget_limit": 10})
    response = await get_client.get(url="/api/v1/categories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1
    assert response.json()[-1]["name"] == "food"


@pytest.mark.asyncio
async def test_get_items(get_client):
    request = await get_client.post(url="/api/v1/items", json={"title": "Phone", "price": 250})
    response = await get_client.get(url="/api/v1/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1
    assert response.json()[-1]["title"] == "Phone"