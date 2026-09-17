import asyncio
import redis.asyncio

SIMULATED_DB = {"book": 40, "ball": 20}


async def get_product_price(product_name: str, client: redis.asyncio.Redis):
    result = await client.get(product_name)
    if result:
        print(f"Cache hit; price: {result}")
        return result
    print("Cache miss")
    price = SIMULATED_DB[product_name]
    await client.set(product_name, price, ex=4)
    return price


async def update_product_price(product_name: str, new_price: int, client: redis.asyncio.Redis):
    SIMULATED_DB[product_name] = new_price
    await client.delete(product_name)
    print(f"DB UPDATED & CACHE INVALIDATED: {product_name} -> {new_price}")


async def main():
    client = redis.asyncio.from_url("redis://localhost:6380", decode_responses=True)
    await get_product_price("book", client)
    await get_product_price("book", client)
    await update_product_price("book", 100, client)
    await get_product_price("book", client)
    await client.aclose()


asyncio.run(main())