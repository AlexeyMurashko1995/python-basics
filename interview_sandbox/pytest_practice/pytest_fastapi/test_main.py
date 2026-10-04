import pytest


@pytest.mark.asyncio
async def test_get_dict(get_client):
    response = await get_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.parametrize("name, price", [
    ("Laptop", 300),
    ("Phone", 200),
    ("Keyboard", 50),
])


@pytest.mark.asyncio
async def test_add_item_parametrize(get_client, name, price):
    response = await get_client.post(url="/items", json={"name": name, "price": price})
    assert response.status_code == 200
    assert response.json() == {"status": "created", "data": {"name": name, "price": price}}


@pytest.mark.asyncio
async def test_add_user(get_client):
    response = await get_client.post(url="/api/v1/users", json={"username": "Alex", "email": "al@gmail.com", "age": 18})
    assert response.status_code == 200
    assert response.json() == {"status": "created", "data": {"username": "Alex", "email": "al@gmail.com", "age": 18}}