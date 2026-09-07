from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel, ConfigDict

engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db():
    async with async_session_factory() as session:
        yield session


class Base(DeclarativeBase):
    pass


class ParcelDB(Base):
    __tablename__ = "parcels"
    id: Mapped[int] = mapped_column(primary_key=True)
    tracking_code: Mapped[str]
    weight: Mapped[float]
    is_delivered: Mapped[bool] = mapped_column(default=False)


class ParcelCreate(BaseModel):
    tracking_code: str
    weight: float
    is_delivered: bool = False


class ParcelResponse(BaseModel):
    id: int
    tracking_code: str
    weight: float
    is_delivered: bool

    model_config = ConfigDict(from_attributes=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield


app = FastAPI(lifespan=lifespan)