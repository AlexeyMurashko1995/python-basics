import asyncio


async def get_transaction(transaction_id: int, failed_transaction: bool):
    print(f"Starting transaction #{transaction_id}")
    await asyncio.sleep(2)
    if failed_transaction:
        raise ValueError("Error")
    return f"id {transaction_id}"


async def main():
    result = await asyncio.gather(get_transaction(1, True), get_transaction(2, False), get_transaction(3, False), get_transaction(4, True), return_exceptions=True)
    for item in result:
        if isinstance(item, Exception):
            print(f"Error: {item}")
        else:
            print(f"Success: {item}")


asyncio.run(main())