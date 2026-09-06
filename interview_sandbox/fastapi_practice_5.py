from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel, ConfigDict
from contextlib import asynccontextmanager


class Base(DeclarativeBase):
    pass


class OrdersDB(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    total_price: Mapped[float]


class OrderCreate(BaseModel):
    user_id: int
    total_price: float


class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_price: float

    model_config = ConfigDict(from_attributes=True)


engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield


app = FastAPI(lifespan=lifespan)


async def get_db():
    async with async_session_factory() as session:
        yield session


async def create_order_in_db(user_id: int, total_price: float, session: AsyncSession):
    if total_price <= 0:
        raise ValueError("Total price must be positive")
    new_order = OrdersDB(user_id=user_id, total_price=total_price)
    session.add(new_order)
    await session.commit()
    await session.refresh(new_order)
    return new_order


async def get_order_by_id(order_id: int, session: AsyncSession):
    result = await session.get(OrdersDB, order_id)
    return result


async def get_all_orders(session: AsyncSession):
    query = select(OrdersDB)
    result = await session.execute(query)
    all_orders = result.scalars().all()
    return all_orders


@app.post("/orders", response_model=OrderResponse)
async def create_order(order_data: OrderCreate, session: AsyncSession = Depends(get_db)):
    try:
        new_order = await create_order_in_db(user_id=order_data.user_id, total_price=order_data.total_price, session=session)
        return new_order
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int, session: AsyncSession = Depends(get_db)):
    target_order = await get_order_by_id(order_id=order_id, session=session)
    if target_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return target_order