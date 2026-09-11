import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


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