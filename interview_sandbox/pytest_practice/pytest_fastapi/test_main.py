import pytest
from main import app, get_api_key, get_data


async def get_fake_api_key():
    return "valid_key"


@pytest.mark.asyncio
async def test_get_data_failure(get_client):
    response = await get_client.get(url="/api/v1/secret_data")
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid API Key"}


@pytest.mark.asyncio
async def test_get_data_success(get_client):
    app.dependency_overrides[get_api_key] = get_fake_api_key
    response = await get_client.get(url="/api/v1/secret_data")
    assert response.status_code == 200
    assert response.json() == {"data": "top_secret_payload"}