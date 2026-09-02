from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
import asyncio

engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_db():
    async with async_session_factory() as session:
        yield session


async def main():
    async for session in get_db():
        print(f"SQL-request over the session: {session}")


asyncio.run(main())