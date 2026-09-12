import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import asyncio


class CartResponse(BaseModel):
    id: int
    total_products: int = Field(validation_alias="totalProducts")
    total_quantity: int = Field(validation_alias="totalQuantity")
    discounted_total: float = Field(validation_alias="discountedTotal")


app = FastAPI()


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


async def get_carts_batch(cart_ids: list[int]) -> list[dict]:
    async with httpx.AsyncClient(timeout=3.0) as client:
        tasks = [fetch_single_cart(client, cart_id) for cart_id in cart_ids]
        results = await asyncio.gather(*tasks)
        return results


@app.post("/carts/batch", response_model=list[CartResponse])
async def get_carts(ids: list[int]):
    try:
        return await get_carts_batch(cart_ids=ids)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))