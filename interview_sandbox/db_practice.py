from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
import asyncio


engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db():
    async with async_session_factory() as session:
        print("[DB LOG]: Session opened")
        yield session
        print("[DB LOG]: Session closed")


async def get_user_by_id(user_id: int, session: AsyncSession):
    if user_id <= 0:
        raise ValueError("Error")
    else:
        return f"Success; user_id:{user_id}"


async def main():
    async for session in get_db():
        id_list = [5, -1]
        for user_id in id_list:
            try:
                result = await get_user_by_id(user_id, session)
                print(result)
            except ValueError:
                print("Error")


asyncio.run(main())

