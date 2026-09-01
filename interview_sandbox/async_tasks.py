import asyncio

async def process_payload(payload_id: int, delay: int):
    print(f"Starting: id {payload_id}")
    await asyncio.sleep(delay)
    if payload_id % 2 == 0:
        raise ValueError(f"Error: id {payload_id}")
    return f"Success: id {payload_id}"


async def main():
    result = await asyncio.gather(process_payload(1, 2), process_payload(2, 2), process_payload(3,3), process_payload(4,1), return_exceptions=True)
    for item in result:
        final = isinstance(item, Exception)
        if final:
            print(f"Error: {item}")
        else:
            print(f"Success: {item}")


asyncio.run(main())