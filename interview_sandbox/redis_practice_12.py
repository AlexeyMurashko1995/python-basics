import asyncio
import redis.asyncio


SIMULATED_DB = {"book": 40, "ball": 20}



async def get_product_price(product_name: str, client: redis.asyncio.Redis):
    result = await client.get(product_name)
    if result:
        print(f"Cache hit: {result}")
        return result
    print(f"Cache Miss: {product_name}")
    price = SIMULATED_DB[product_name]
    await client.set(product_name, price, ex=3)
    return price


async def main():
    client = redis.asyncio.from_url("redis://localhost:6380", decode_responses=True)
    await get_product_price("book", client)
    await get_product_price("book", client)
    await asyncio.sleep(4)
    await get_product_price("book", client)
    await client.aclose()


asyncio.run(main())