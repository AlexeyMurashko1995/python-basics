import asyncio
import time

# async def process_payload(payload_id: int, delay: int):
#     print(f"Starting: id {payload_id}")
#     await asyncio.sleep(delay)
#     if payload_id % 2 == 0:
#         raise ValueError(f"Error: id {payload_id}")
#     return f"Success: id {payload_id}"


# async def main():
#     result = await asyncio.gather(process_payload(1, 2), process_payload(2, 2), process_payload(3,3), process_payload(4,1), return_exceptions=True)
#     for item in result:
#         final = isinstance(item, Exception)
#         if final:
#             print(f"Error: {item}")
#         else:
#             print(f"Success: {item}")


# asyncio.run(main())

# def sync_heavy_task():
#     print("Sync task started")
#     time.sleep(2)
#     print("Sync task finished")


# async def fast_async_task():
#     await asyncio.sleep(1)
#     print("Fast task .....")


# async def main():
#     result = await asyncio.gather(asyncio.to_thread(sync_heavy_task), fast_async_task())


# asyncio.run(main())


async def fetch_user_from_db(user_id: int):
    print(f"Session with id {user_id}")
    await asyncio.sleep(1)
    if user_id < 0:
        raise ValueError("Invalid ID")
    elif user_id == 0:
        raise ConnectionError("Connection failed")
    return {"user_id": user_id, "status": "active"}

async def main():
    user_id = [10, 0, -5]
    for id in user_id:
        try:
            result = await fetch_user_from_db(id)
            print(f"Success: {result}")
        except ValueError as e:
            print(f"[VALIDATION ERROR]: {e}")
        except ConnectionError as e:
            print(f"[DB ERROR]: {e}")


asyncio.run(main())