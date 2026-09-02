import asyncio

async def get_db():
    print("[DB]: Connection opened")
    try:
        yield "AsyncSession_Object"
    finally:
        print("[DB]: Connection closed")


async def main():
    async for session in get_db():
        print(f"Our session: {session}")
        raise ValueError("Error in the endpoint")

asyncio.run(main())
