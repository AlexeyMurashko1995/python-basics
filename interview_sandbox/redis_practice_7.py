import asyncio
import redis
import time


FAKE_PRODUCTS_DB = {1: {"id": 1, "name": "book", "price": 120}}

SIMULATED_REDIS = {}


async def get_product_from_db(product_id: int):
    await asyncio.sleep(2)
    return FAKE_PRODUCTS_DB[product_id]


async def read_product(product_id: int, ttl_seconds: int = 4):
    if product_id in SIMULATED_REDIS and time.time() - SIMULATED_REDIS[product_id]["created_at"] < ttl_seconds:
        print("CACHE HIT")
        return SIMULATED_REDIS[product_id]["data"]
    print("CACHE MISS")
    product = await get_product_from_db(product_id=product_id)
    SIMULATED_REDIS[product_id] = {"data": product, "created_at": time.time()}
    return product