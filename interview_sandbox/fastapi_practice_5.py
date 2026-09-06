from fastapi import FastAPI
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


