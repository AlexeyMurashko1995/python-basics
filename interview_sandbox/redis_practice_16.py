import asyncio
import random
import redis.asyncio


async def set_with_jitter(client: redis.asyncio.Redis, key: str, value: str, base_ttl: int = 5, max_jitter: int = 3):
    random_time = base_ttl + random.randint(1, max_jitter)
    await client.set(key, value, ex=random_time)
    print(f"SAVED: {key} with TTL={random_time}")


async def main():
    client = redis.asyncio.from_url("redis://localhost:6380", decode_responses=True)
    i = 1
    for _ in range(5):
        await set_with_jitter(client, f"item_{i}", 2)
        i += 1
    await client.aclose()


asyncio.run(main())