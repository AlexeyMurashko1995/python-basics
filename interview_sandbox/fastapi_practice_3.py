from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from fastapi import FastAPI
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class PaymentDB(Base):
    __tablename__ = "payments"
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int]
    amount: Mapped[float]