import asyncio
import redis

SIMULATED_DB = {"product_1": 100}

SIMULATED_REDIS = {}


async def get_product_price(product_id: str):
    if product_id in SIMULATED_REDIS:
        print("CACHE HIT")
        return SIMULATED_REDIS[product_id]
    print("CACHE MISS")
    product_price = SIMULATED_DB[product_id]
    SIMULATED_REDIS[product_id] = product_price
    return product_price