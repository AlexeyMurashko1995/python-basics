import asyncio
import random
import redis.asyncio


SIMULATED_DB = {"laptop": 1500, "mouse": 25}


async def set_with_jitter(client: redis.asyncio.Redis, key: str, value: int, base_ttl: int = 10, max_jitter: int = 5):
    random_ttl = base_ttl + random.randint(1, max_jitter)
    await client.set(key, value, ex=random_ttl)
    print(f"Jitter set. Name: {key}, ttl: {random_ttl}")


async def get_product_price(product_name: str, client: redis.asyncio.Redis):
    price = await client.get(product_name)
    if price:
        print("[CACHE HIT]")
        return price
    print(f"[CACHE MISS]")
    got_lock = await client.set(f"lock:{product_name}", "1", nx=True, ex=5)
    if got_lock:
        price = SIMULATED_DB[product_name]
        await set_with_jitter(client, product_name, price)
        await client.delete(f"lock:{product_name}")
        return price
    await asyncio.sleep(0.1)
    return await get_product_price(product_name, client)


async def update_product_price(product_name: str, new_price: int, client: redis.asyncio.Redis):
    SIMULATED_DB[product_name] = new_price
    await client.delete(product_name)
    print(f"Price updated. Product: {product_name}; New price: {new_price}")


async def main():
    client = redis.asyncio.from_url("redis://localhost:6380", decode_responses=True)
    await client.delete("laptop")
    await asyncio.gather(get_product_price("laptop", client), get_product_price("laptop", client))
    await update_product_price("laptop", 1700, client)
    await get_product_price("laptop",client)
    await client.aclose()


asyncio.run(main())