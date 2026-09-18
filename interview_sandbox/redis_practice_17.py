import asyncio
import redis.asyncio

SIMULATED_DB = {"phone": 600}


async def get_product_price_safe(product_name: str, client: redis.asyncio.Redis):
    price = await client.get(product_name)
    if price:
        print("CACHE HIT")
        print(f"{product_name}'s price: {price}")
        return price

    print(f"CACHE MISS: {product_name}")
    got_lock = await client.set(f"lock:{product_name}", "1", nx=True, ex=5)

    if got_lock:
        print("LOCK ACQUIRED: Reading from DB...")
        price = SIMULATED_DB[product_name]
        await client.set(product_name, price, ex=5)
        await client.delete(f"lock:{product_name}")
        return price

    print("LOCK BUSY: Waiting...")
    await asyncio.sleep(0.1)
    return await get_product_price_safe(product_name, client)


async def main():
    client = redis.asyncio.from_url("redis://localhost:6380", decode_responses=True)
    await client.delete("phone")

    result = await asyncio.gather(
        get_product_price_safe("phone", client),
        get_product_price_safe("phone", client),
    )
    print(result)

    await client.aclose()


if __name__ == "__main__":
    asyncio.run(main())