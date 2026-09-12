import httpx
from fastapi import FastAPI
from pydantic import BaseModel, Field


class CartResponse(BaseModel):
    id: int
    total_products: int = Field(validation_alias="totalProducts")
    total_quantity: int = Field(validation_alias="totalQuantity")
    discounted_total: float = Field(validation_alias="discountedTotal")


async def fetch_single_cart(client: httpx.AsyncClient, cart_id: int) -> dict:
    try:
        response = await client.get(url=f"https://dummyjson.com/carts/{cart_id}")
        if response.status_code == 404:
            raise ValueError("Cart not found")
        return response.json()
    except httpx.TimeoutException:
        raise ValueError("Server timed out")
    except httpx.RequestError:
        raise ValueError("Server unavailable")