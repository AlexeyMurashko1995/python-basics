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


@pytest.mark.parametrize("name, email, age", [
    ("Alex", "am@gmail.com", 18),
    ("Elena", "el@mail.ru", 25),
    ("Ivan", "il@gmail.com", 15),
])


@pytest.mark.asyncio
async def test_add_user_parametrize_success(get_client, name, email, age):
    response = await get_client.post(url="/api/v1/users", json={"username": name, "email": email, "age": age})
    assert response.status_code == 200
    assert response.json() == {"status": "created", "data": {"username": name, "email": email, "age": age}}


@pytest.mark.parametrize("name, email, age", [
    ("Alex", "am@gmail.com", ""),
    ("Elena", "em@mail.com", "eighteen"),
    ("", "", ""),
])


@pytest.mark.asyncio
async def test_add_user_invalid_data(get_client, name, email, age):
    response = await get_client.post(url="/api/v1/users", json={"username": name, "email": email, "age": age})
    assert response.status_code == 422
