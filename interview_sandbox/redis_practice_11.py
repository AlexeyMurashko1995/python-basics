import asyncio
import redis.asyncio


async def main():
    client = redis.asyncio.from_url("redis://localhost:6380", decode_responses=True)
    await client.set("course", "Python_AI", ex=3)
    print(await client.get("course"))
    await asyncio.sleep(4)
    print(await client.get("course"))
    await client.aclose()


asyncio.run(main())