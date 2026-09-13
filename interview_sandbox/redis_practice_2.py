import asyncio
import redis
import time

SIMULATED_REDIS = {}


async def fetch_product_from_db(product_id: int):
    await asyncio.sleep(2)
    return {"id": product_id, "price": 100}


async def get_product(product_id: int, ttl_seconds: int = 5):
    if product_id in SIMULATED_REDIS and time.time() - SIMULATED_REDIS[product_id]["created_at"] < ttl_seconds:
        print("[CACHE HIT]")
        return SIMULATED_REDIS[product_id]["data"]
    print("CACHE MISS")
    product = await fetch_product_from_db(product_id=product_id)
    SIMULATED_REDIS[product_id] = {"data": product, "created_at": time.time()}
    return product


async def main():
    await get_product(1, ttl_seconds=5)
    await get_product(1, ttl_seconds=5)
    await asyncio.sleep(6)
    await get_product(1, ttl_seconds=5)


asyncio.run(main())