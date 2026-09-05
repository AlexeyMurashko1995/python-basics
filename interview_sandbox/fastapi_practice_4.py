from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass