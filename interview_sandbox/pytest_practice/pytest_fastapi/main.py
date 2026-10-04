from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CreateItem(BaseModel):
    name: str
    price: float


class UserCreate(BaseModel):
    username: str
    email: str
    age: int


@app.get("/health")
async def get_dict():
    return {"status": "ok"}


@app.post("/items")
async def add_item(item_data: CreateItem):
    return {"status": "created", "data": {"name": item_data.name, "price": item_data.price}}


@app.post("/api/v1/users")
async def add_user(user_data: UserCreate):
    return {"status": "created", "data": {"username": user_data.username, "email": user_data.email, "age": user_data.age}}