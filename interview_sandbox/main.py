import asyncio

async def simple_task():
    print("Starting work...")
    await asyncio.sleep(2)
    result = "Finishing..."
    return result


async def main():
    res1 = await simple_task()
    res2 = await simple_task()
    print(res1, res2)


asyncio.run(main())