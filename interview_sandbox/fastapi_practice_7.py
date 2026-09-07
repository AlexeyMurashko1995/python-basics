from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import select
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


async def create_parcel_in_db(tracking_code: str, weight: float, is_delivered: bool, session: AsyncSession):
    if len(tracking_code.strip()) < 5:
        raise ValueError("At least 5 symbols")
    if weight <= 0:
        raise ValueError("Weight must be only positive")
    new_parcel = ParcelDB(tracking_code=tracking_code, weight=weight, is_delivered=is_delivered)
    session.add(new_parcel)
    await session.commit()
    await session.refresh(new_parcel)
    return new_parcel


async def get_parcel_by_id(parcel_id: int, session: AsyncSession):
    target_parcel = await session.get(ParcelDB, parcel_id)
    return target_parcel


async def get_all_parcels(session: AsyncSession):
    query = select(ParcelDB)
    result = await session.execute(query)
    all_parcels = result.scalars().all()
    return all_parcels


async def delete_parcel_by_id(parcel_id: int, session: AsyncSession):
    target_parcel = await session.get(ParcelDB, parcel_id)
    if target_parcel is not None:
        result = session.delete(target_parcel)
        await session.commit()
        return True
    return False