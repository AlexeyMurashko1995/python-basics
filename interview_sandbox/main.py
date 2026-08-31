import asyncio


async def get_delay(id_source: int, is_error: bool):
    print(f"Starting {id_source} id")
    await asyncio.sleep(1)
    if not is_error:
        return f"Finishing {id_source} id"
    raise ValueError("Error")


async def main():
    result = await asyncio.gather(get_delay(1, False), get_delay(2, True), get_delay(3, False), return_exceptions=True)
    for item in result:
        if isinstance(item, Exception):
            print(f"Failed: {item}")
        else:
            print(f"Success: {item}")


asyncio.run(main())