from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

engine = create_async_engine("sqlite+aiosqlite:///:memory:")

app = FastAPI()

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_db():
    async with async_session_factory() as session:
        print("Session opened")
        yield session
        print("Session closed")


class OrderCreate(BaseModel):
    product_name: str
    quantity: int


async def process_order(product_name: str, quantity: int, session: AsyncSession):
    if quantity <= 0:
        raise ValueError("Error of quantity")
    elif product_name == "out_of_stock":
        raise KeyError("Out of stock")
    else:
        return f"Your order for {product_name} successfully confirmed"


@app.post("/orders")
async def create_order(payload: OrderCreate, session: AsyncSession = Depends(get_db)):
    try:
        result = await process_order(product_name=payload.product_name, quantity=payload.quantity, session=session)
        return {"status": "ok", "message": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Error of quantity")
    except KeyError:
        raise HTTPException(status_code=404, detail="Out of stock")
