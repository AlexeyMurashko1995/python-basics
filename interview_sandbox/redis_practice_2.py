import asyncio
import redis

SIMULATED_REDIS = {}


async def fetch_product_from_db(product_id: int):
    await asyncio.sleep(2)
    return {"id": product_id, "price": 100}


async def get_product(product_id: int):
    if product_id in SIMULATED_REDIS:
        print("[CACHE HIT]")
        return SIMULATED_REDIS[product_id]
    print("[CACHE MISS]")
    product = await fetch_product_from_db(product_id=product_id)
    SIMULATED_REDIS[product_id] = product
    return product


async def main():
    await get_product(10)
    await get_product(10)


asyncio.run(main())