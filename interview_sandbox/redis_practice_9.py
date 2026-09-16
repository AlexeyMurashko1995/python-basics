import redis
import asyncio

SIMULATED_REDIS = {}

db_lock = asyncio.Lock()


async def get_user_from_db(user_id: int):
    print("[DB CALL]")
    await asyncio.sleep(2)
    return {"id": user_id, "data": f"User: {user_id}"}


async def get_data(user_id: int):
    if user_id in SIMULATED_REDIS:
        print("CACHE HIT")
        return SIMULATED_REDIS[user_id]["data"]
    async with db_lock:
        if user_id in SIMULATED_REDIS:
            print("CACHE HIT AFTER LOCK")
            return SIMULATED_REDIS[user_id]["data"]
        print("CACHE MISS")
        user_data = await get_user_from_db(user_id=user_id)
        SIMULATED_REDIS[user_id] = user_data
        return user_data["data"]


async def main():
    results = await asyncio.gather(get_data(1), get_data(1), get_data(1), get_data(1), get_data(1))
    print(results)


asyncio.run(main())



