import pytest
from main import app, get_current_user, get_discount


async def fake_get_current_user():
    return {"role": "admin"}


async def fake_get_discount():
    return 0.2


@pytest.mark.asyncio
async def test_get_profile_with_override(get_client):
    app.dependency_overrides[get_current_user] = fake_get_current_user
    response = await get_client.get("/api/v1/profile")
    assert response.status_code == 200
    assert response.json() == {"user": {"role": "admin"}}


@pytest.mark.asyncio
async def test_get_discount_without_override(get_client):
    response = await get_client.post(url="/api/v1/checkout", json={"price": 100})
    assert response.json() == {"final_price": 100}


@pytest.mark.asyncio
async def test_get_discount_with_override(get_client):
    app.dependency_overrides[get_discount] = fake_get_discount
    response = await get_client.post(url="/api/v1/checkout", json={"price": 100})
    assert response.json() == {"final_price": 80}