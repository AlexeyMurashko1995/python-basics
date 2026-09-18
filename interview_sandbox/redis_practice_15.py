import asyncio
import redis.asyncio


SIMULATED_DB = {"keyboard": 100, "mouse": 50}


async def get_product_price(product_name: str, client: redis.asyncio.Redis):
    product = await client.get(product_name)
    if product:
        print("CACHE HIT")
        print(f"Product price: {product}")
        return product
    print("CACHE MISS")
    product = SIMULATED_DB[product_name]
    await client.set(product_name, product, ex=5)
    return product


async def update_product_price(product_name: str, new_price: int, client: redis.asyncio.Redis):
    SIMULATED_DB[product_name] = new_price
    await client.delete(product_name)
    print(f"Product name: {product_name}; updated price: {new_price}")


async def main():
    client = redis.asyncio.from_url("redis://localhost:6380", decode_responses=True)
    await get_product_price("keyboard", client)
    await get_product_price("keyboard", client)
    await update_product_price("keyboard", 120, client)
    await get_product_price("keyboard", client)
    await client.aclose()


asyncio.run(main())