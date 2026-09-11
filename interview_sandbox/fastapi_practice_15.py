import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import asyncio


class ProductResponse(BaseModel):
    id: int
    title: str
    discount_percentage: float = Field(validation_alias="discountPercentage")


app = FastAPI()


async def get_single_product(client: httpx.AsyncClient, product_id: int) -> dict:
    try:
        response = await client.get(url=f"https://dummyjson.com/products/{product_id}")
        if response.status_code == 404:
            raise ValueError("Product not found")
        return response.json()
    except httpx.TimeoutException:
        raise ValueError("Server timed out")
    except httpx.RequestError:
        raise ValueError("Server is unavailable")


async def get_products_batch(products_id: list[int]) -> list[dict]:
    async with httpx.AsyncClient(timeout=3.0) as client:
        products_to_get = [get_single_product(client, product_id) for product_id in products_id]
        results = await asyncio.gather(*products_to_get)
        return results


@app.post("/products/batch", response_model= list[ProductResponse])
async def get_products_together(ids: list[int]):
    try:
        return await get_products_batch(products_id=ids)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))