import asyncio

async def worker(name: str, delay: int):
    print(f"Start: {name}")
    await asyncio.sleep(delay)
    return f"Finish: {name}"

async def main():
    task1 = asyncio.create_task(worker("A", 3))
    task2 = asyncio.create_task(worker("B", 1))
    print("Control to the Event Loop")
    result2 = await task2
    print(result2)
    result1 = await task1
    print(result1)

asyncio.run(main())