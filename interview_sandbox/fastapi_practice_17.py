import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio


class QuoteResponse(BaseModel):
    id: int
    quote: str
    author: str


app = FastAPI()


async def get_single_quote(client: httpx.AsyncClient, quote_id: int) -> dict:
    try:
        response = await client.get(url=f"https://dummyjson.com/quotes/{quote_id}")
        if response.status_code == 404:
            raise ValueError("Quote not found")
        return response.json()
    except httpx.TimeoutException:
        raise ValueError("Server timed out")
    except httpx.RequestError:
        raise ValueError("Server is not available")


async def get_quotes_batch(quote_ids: list[int]) -> list[dict]:
    async with httpx.AsyncClient(timeout=3.0) as client:
        tasks = [get_single_quote(client, quote_id) for quote_id in quote_ids]
        results = await asyncio.gather(*tasks)
        return results


@app.post("/quotes/batch", response_model=list[QuoteResponse])
async def get_batch(ids: list[int]):
    try:
        return await get_quotes_batch(quote_ids=ids)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))