from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
import asyncio

engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_db():
    async with async_session_factory() as session:
        print("Session opened.")
        yield session
        print("Session closed")


async def process_payment(payment_amount: int, account_name: str, session: AsyncSession):
    if payment_amount <= 0:
        raise ValueError("Error")
    elif account_name == "banned":
        raise PermissionError("Ban_error!")
    return f"payment {payment_amount} for {account_name} completed"


async def main():
    cases = [
        (120, "Alex"),
        (0, "Ivan"),
        (20, "banned")
    ]
    for amount, name in cases:
        async for session in get_db():
            try:
                result = await process_payment(amount, name, session)
                print(result)
            except ValueError:
                print("Value Error")
            except PermissionError:
                print("PermissionError")



asyncio.run(main())