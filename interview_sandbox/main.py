import asyncio

async def simple_task():
    print("Starting work...")
    await asyncio.sleep(2)
    print("Finishing")


async def main():
    result = await asyncio.gather(simple_task(), simple_task())
    print(result)


asyncio.run(main())