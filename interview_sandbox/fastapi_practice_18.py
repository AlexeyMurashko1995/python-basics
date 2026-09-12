import asyncio
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class RecipeSummaryResponse(BaseModel):
    id: int
    name: str
    prep_time_minutes: int = Field(validation_alias="prepTimeMinutes")
    is_quick: bool


app = FastAPI()


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


async def fetch_recipes_batch(recipe_ids: list[int]) -> list[dict]:
    async with httpx.AsyncClient(timeout=3.0) as client:
        tasks = [fetch_single_recipe(client, recipe_id) for recipe_id in recipe_ids]
        results = await asyncio.gather(*tasks)
        for result in results:
            if result["prepTimeMinutes"] <= 15:
                result["is_quick"] = True
            else:
                result["is_quick"] = False
        return results


@app.post("/recipes/batch", response_model=list[RecipeSummaryResponse])
async def get_all_recipes(ids: list[int]):
    try:
        return await fetch_recipes_batch(recipe_ids=ids)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))