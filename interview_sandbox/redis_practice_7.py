import asyncio
import redis
import time


FAKE_PRODUCTS_DB = {1: {"id": 1, "name": "book", "price": 120}}

SIMULATED_REDIS = {}


async def get_product_from_db(product_id: int):
    await asyncio.sleep(2)
    return FAKE_PRODUCTS_DB[product_id]


async def read_product(product_id: int):
    pass