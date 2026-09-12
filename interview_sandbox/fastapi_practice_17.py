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

