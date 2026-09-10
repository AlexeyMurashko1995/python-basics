from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel


app = FastAPI()

class ExternalProductResponse(BaseModel):
    id: int
    title: str
    price: float


async def fetch_external_product(product_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url=f"https://dummyjson.com/products/{product_id}")
        if response.status_code == 404:
            raise ValueError("External product not found")
        return response.json()


@app.get("/external-products/{product_id}", response_model=ExternalProductResponse)
async def get_external_product(product_id: int):
    try:
        ext_product = await fetch_external_product(product_id=product_id)
        return ext_product
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))