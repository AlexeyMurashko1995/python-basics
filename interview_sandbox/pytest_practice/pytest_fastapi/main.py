from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CreateItem(BaseModel):
    name: str
    price: float


@app.get("/health")
async def get_dict():
    return {"status": "ok"}


@app.post("/items")
async def add_item(item_data: CreateItem):
    return {"status": "created", "data": {"name": item_data.name, "price": item_data.price}}