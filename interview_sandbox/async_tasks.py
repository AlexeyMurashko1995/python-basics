import asyncio

async def fetch_data(db_name: str, delay: int):
    print(f"Request to {db_name}")
    await asyncio.sleep(delay)
    return f"Data from {db_name}"

async def main():
    task1 = asyncio.create_task(fetch_data("Users", 2))
    task2 = asyncio.create_task(fetch_data("Orders", 1))
    print("Event Loop is working...")
    resul1 = await task1
    result2 = await task2
    print(resul1, result2)


asyncio.run(main())