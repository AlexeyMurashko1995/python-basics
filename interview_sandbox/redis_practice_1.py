import redis
import asyncio


SIMULATED_REDIS = {}


async def fetch_user_from_db(user_id: int):
    await asyncio.sleep(2)
    return {"id": user_id, "name": f"User_{user_id}"}


async def get_user(user_id: int):
    if user_id in SIMULATED_REDIS:
        print("[CACHE HIT]")
        return SIMULATED_REDIS[user_id]
    print("[CACHE MISS]")
    user = await fetch_user_from_db(user_id=user_id)
    SIMULATED_REDIS[user_id] = user
    return user


async def main():
    await get_user(1)
    await get_user(1)


asyncio.run(main())