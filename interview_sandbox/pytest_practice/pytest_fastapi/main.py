from fastapi import Depends, FastAPI
from pydantic import BaseModel


app = FastAPI()


class OrderCreate(BaseModel):
    price: float


async def get_current_user():
    return {"role": "guest"}


async def get_discount():
    return 0.0


@app.get("/api/v1/profile")
async def get_profile(user = Depends(get_current_user)):
    return {"user": user}


@app.post("/api/v1/checkout")
async def create_order(order_data: OrderCreate, discount = Depends(get_discount)):
    final_price = order_data.price * (1 - discount)
    return {"final_price": final_price}
