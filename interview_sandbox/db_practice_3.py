from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
import asyncio

engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db():
    async with async_session_factory() as session:
        print("Session opened")
        yield session
        print("Session closed")


async def process_order(product_name: str, quantity: int, session: AsyncSession):
    if quantity <= 0:
        raise ValueError("ValueError")
    elif product_name == "out_of_stock":
        raise KeyError("KeyError")
    else:
        return f"Your order for {product_name} successfully confirmed"


async def main():
    cases = [
        ("laptop", 2),
        ("out_of_stock", 1),
        ("phone", -1)
    ]
    for name, quantity in cases:
        async for session in get_db():
            try:
                result = await process_order(name, quantity, session)
                print(result)
            except ValueError:
                print("Err1")
            except KeyError:
                print("Err2")


asyncio.run(main())