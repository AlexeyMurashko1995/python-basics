import asyncio

async def get_stream():
    print("Stream opened")
    try:
        yield "Stream_Object"
    finally:
        print("Stream closed")


async def main():
    async for stream in get_stream():
        print(f"Result: {stream}")
        raise RuntimeError("Error")


asyncio.run(main())