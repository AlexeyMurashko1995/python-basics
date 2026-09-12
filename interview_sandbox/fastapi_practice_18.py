import httpx
from fastapi import FastAPI
from pydantic import BaseModel, Field


class RecipeSummaryResponse(BaseModel):
    id: int
    name: str
    prep_time_minutes: int = Field(validation_alias="prepTimeMinutes")
    is_quick: bool


async def fetch_single_recipe(client: httpx.AsyncClient, recipe_id: int) -> dict:
    try:
        response = await client.get(url=f"https://dummyjson.com/recipes/{recipe_id}")
        if response.status_code == 404:
            raise ValueError("Recipe not found")
        return response.json()
    except httpx.TimeoutException:
        raise ValueError("Server timed out")
    except httpx.RequestError:
        raise ValueError("Server is not available")
