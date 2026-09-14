import asyncio
import redis
import time


SIMULATED_REDIS = {}


async def get_profile_from_db(profile_id: int):
    await asyncio.sleep(2)
    return {"id": profile_id, "description": f"Desc: {profile_id}"}


async def read_profile(profile_id: int, ttl_seconds: int = 3):
    if profile_id in SIMULATED_REDIS and time.time() - SIMULATED_REDIS[profile_id]["created_at"] < ttl_seconds:
        print("CACHE HIT")
        return SIMULATED_REDIS[profile_id]["data"]
    print("CACHE MISS")
    profile = await get_profile_from_db(profile_id=profile_id)
    SIMULATED_REDIS[profile_id] = {"data": profile, "created_at": time.time()}
    return profile


async def update_profile(profile_id: int, email: str):
    if profile_id in SIMULATED_REDIS:
        del SIMULATED_REDIS[profile_id]
    return {"id": profile_id, "email": email}


async def main():
    await read_profile(42)
    await read_profile(42)
    await update_profile(42, "iv@gmail.com")
    await read_profile(42)


asyncio.run(main())