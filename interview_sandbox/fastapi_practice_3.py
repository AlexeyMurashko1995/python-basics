from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from fastapi import FastAPI
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel, ConfigDict


engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield


app = FastAPI(lifespan=lifespan)

class Base(DeclarativeBase):
    pass


class PaymentDB(Base):
    __tablename__ = "payments"
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int]
    amount: Mapped[float]


class PaymentCreate(BaseModel):
    account_id: int
    amount: float


class PaymentResponse(BaseModel):
    id: int
    account_id: int
    amount: float
    model_config = ConfigDict(from_attributes=True)


async def get_db():
    async with async_session_factory() as session:
        yield session


async def create_payment_in_db(account_id: int, amount: float, session: AsyncSession):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    new_payment = PaymentDB(account_id=account_id, amount=amount)
    session.add(new_payment)
    await session.commit()
    await session.refresh(new_payment)
    return new_payment


