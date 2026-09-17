import asyncio
import redis.asyncio

SIMULATED_DB = {"laptop": 1200, "phone": 800}


async def get_product_price(product_name: str, client: redis.asyncio.Redis):
    query = await client.get(product_name)
    if query:
        print(f"CACHE HIT! Price: {query}")
        return query
    print("CACHE MISS")
    price = SIMULATED_DB[product_name]
    await client.set(product_name, price, ex=4)
    return price


async def update_product_price(product_name: str, new_price: int, client: redis.asyncio.Redis):
    SIMULATED_DB[product_name] = new_price
    await client.delete(product_name)
    print(f"CACHE INVALIDATED: {product_name} -> {new_price}")


async def main():
    client = redis.asyncio.from_url("redis://localhost:6380", decode_responses=True)

    await get_product_price("laptop", client)
    await get_product_price("laptop", client)
    await update_product_price("laptop", 1300, client)
    await get_product_price("laptop", client)
    await client.aclose()


asyncio.run(main())