from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel


app = FastAPI()


class UserPortfelResponse(BaseModel):
    id: int
    firstName: str
    email: str
    age: int


async def get_user_portfel(user_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url=f"https://dummyjson.com/users/{user_id}")
        if response.status_code == 404:
            raise ValueError("User not found")
        return response.json()


@app.get("/external-users/{user_id}", response_model=UserPortfelResponse)
async def get_portfel(user_id: int):
    try:
        result = await get_user_portfel(user_id=user_id)
        return result
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))