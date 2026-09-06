from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel, ConfigDict


engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass


class ProductDB(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    price: Mapped[float]
    is_available: Mapped[bool] = mapped_column(default=True)


class ProductCreate(BaseModel):
    title: str
    price: float
    is_available: bool = True


class ProductResponse(BaseModel):
    id: int
    title: str
    price: float
    is_available: bool

    model_config = ConfigDict(from_attributes=True)

async def get_db():
    async with async_session_factory() as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield


app = FastAPI(lifespan=lifespan)