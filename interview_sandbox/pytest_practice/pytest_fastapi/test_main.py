import pytest
from main import app, get_current_user


async def fake_get_current_user():
    return {"role": "admin"}


@pytest.mark.asyncio
async def test_get_profile_with_override(get_client):
    app.dependency_overrides[get_current_user] = fake_get_current_user
    response = await get_client.get("/api/v1/profile")
    assert response.status_code == 200
    assert response.json() == {"user": {"role": "admin"}}