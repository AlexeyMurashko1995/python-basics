import asyncio
import redis


SIMULATED_DB = {"book": 50, "ball": 60}

SIMULATED_REDIS = {}


async def get_product_price(product_name: str):
    if product_name in SIMULATED_REDIS:
        print("CACHE HIT")
        return SIMULATED_REDIS[product_name]
    print("CACHE MISS")
    product_price = SIMULATED_DB[product_name]
    SIMULATED_REDIS[product_name] = product_price
    return product_price


async def update_product_price(product_name: str, new_price: int):
    SIMULATED_DB[product_name] = new_price
    SIMULATED_REDIS.pop(product_name, None)
    return SIMULATED_DB[product_name]


async def main():
    await get_product_price("book")
    await get_product_price("book")
    await update_product_price("book", 20)
    await get_product_price("book")
    await update_product_price("ball", 900)


asyncio.run(main())
