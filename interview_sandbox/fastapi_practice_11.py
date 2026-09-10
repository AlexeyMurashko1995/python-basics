import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class RecipeResponse(BaseModel):
    id: int
    name: str
    prep_time_minutes: int = Field(validation_alias="prepTimeMinutes")
    cook_time_minutes: int = Field(validation_alias="cookTimeMinutes")
    rating: float


app = FastAPI()


async def get_external_recipe(recipe_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url=f"https://dummyjson.com/recipes/{recipe_id}")
        if response.status_code == 404:
            raise ValueError("Recipe not found")
        return response.json()


@app.get("/recipes/{recipe_id}", response_model=RecipeResponse)
async def get_recipe(recipe_id: int):
    try:
        recipe = await get_external_recipe(recipe_id=recipe_id)
        return recipe
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))
