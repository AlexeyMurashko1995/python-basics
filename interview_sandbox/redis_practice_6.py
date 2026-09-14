import asyncio
import redis
import time


FAKE_DB = {101: {"id": 101, "name": "Alice", "role": "Developer"}}

SIMULATED_REDIS = {}


async def get_user(user_id: int, ttl_seconds: int = 5):
    if user_id in SIMULATED_REDIS and time.time() - SIMULATED_REDIS[user_id]["created_at"] < ttl_seconds:
        print("CACHE HIT")
        return SIMULATED_REDIS[user_id]["data"]
    print("CACHE MISS")
    await asyncio.sleep(2)
    user = FAKE_DB[user_id]
    SIMULATED_REDIS[user_id] = {"data": user, "created_at": time.time()}
    return user


async def update_user_role(user_id: int, new_role: str):
    await asyncio.sleep(1)
    FAKE_DB[user_id]["role"] = new_role
    if user_id in SIMULATED_REDIS:
        del SIMULATED_REDIS[user_id]
    return FAKE_DB[user_id]


async def main():
    await get_user(101)
    await get_user(101)
    await update_user_role(101, "Team Lead")
    await get_user(101)


asyncio.run(main())