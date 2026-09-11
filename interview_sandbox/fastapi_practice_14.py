import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import asyncio


class CommentResponse(BaseModel):
    id: int
    body: str
    post_id: int = Field(validation_alias="postId")


app = FastAPI()


async def get_single_comment(client: httpx.AsyncClient, comment_id: int) -> dict:
    response = await client.get(f"https://dummyjson.com/comments/{comment_id}")
    if response.status_code == 404:
        raise ValueError("Comment not found")
    return response.json()


async def get_comments_batch(comment_ids: list[int]) -> list[dict]:
    async with httpx.AsyncClient(timeout=3.0) as client:
        try:
            tasks = [get_single_comment(client, comment_id) for comment_id in comment_ids]
            results = await asyncio.gather(*tasks)
            return results
        except httpx.TimeoutException:
            raise ValueError("Server timed out")
        except httpx.RequestError:
            raise ValueError("Server unavailable")


@app.post("/comments/batch", response_model=list[CommentResponse])
async def get_comments_gather(ids: list[int]):
    try:
        final_result = await get_comments_batch(comment_ids=ids)
        return final_result
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))