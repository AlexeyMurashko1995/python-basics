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


@pytest.mark.asyncio
async def test_add_user(get_client):
    response = await get_client.post(url="/api/v1/users", json={"username": "Alex", "email": "al@gmail.com", "age": 18})
    assert response.status_code == 200
    assert response.json() == {"status": "created", "data": {"username": "Alex", "email": "al@gmail.com", "age": 18}}