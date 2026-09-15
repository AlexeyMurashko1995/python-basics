import asyncio
import redis
import time


SIMULATED_REDIS = {}

db_lock = asyncio.Lock()


async def get_data_from_db(data_id: int):
    print("[DB CALL]")
    await asyncio.sleep(2)
    return {"id": data_id, "data": f"Heavy Payload #{data_id}"}


async def get_data(data_id: int):
    if data_id in SIMULATED_REDIS:
        print("CACHE HIT")
        return SIMULATED_REDIS[data_id]
    async with db_lock:
        if data_id in SIMULATED_REDIS:
            print("CACHE HIT (AFTER LOCK)")
            return SIMULATED_REDIS[data_id]
        data = await get_data_from_db(data_id=data_id)
        SIMULATED_REDIS[data_id] = data
        return SIMULATED_REDIS[data_id]


async def main():
    results = await asyncio.gather(
        get_data(1),
        get_data(1),
        get_data(1),
        get_data(1),
        get_data(1),
    )
    print("ALL DONE:", len(results))


asyncio.run(main())