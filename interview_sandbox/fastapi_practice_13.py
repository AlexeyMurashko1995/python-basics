import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class CommentResponse(BaseModel):
    id: int
    body: str
    post_id: int = Field(validation_alias="postId")


app = FastAPI()


async def get_external_comment(comment_id: int) -> dict:
    async with httpx.AsyncClient(timeout=2.0) as client:
        try:
            response = await client.get(url=f"https://dummyjson.com/comments/{comment_id}")
            if response.status_code == 404:
                raise ValueError("Comment not found")
            return response.json()
        except httpx.TimeoutException:
            raise ValueError("Service timed out")
        except httpx.RequestError:
            raise ValueError("Service unavailable")


@app.get("/comments/{comment_id}", response_model = CommentResponse)
async def get_target_comment(comment_id: int):
    try:
        target_comment = await get_external_comment(comment_id=comment_id)
        return target_comment
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))