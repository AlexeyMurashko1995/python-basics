from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel, Field


class PostResponse(BaseModel):
    id: int
    title: str
    body: str
    user_id: int = Field(validation_alias="userId")


app = FastAPI()


async def get_external_post(post_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url=f"https://dummyjson.com/posts/{post_id}")
        if response.status_code == 404:
            raise ValueError("Post not found")
        return response.json()


@app.get("/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int):
    try:
        target_post = await get_external_post(post_id=post_id)
        return target_post
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))