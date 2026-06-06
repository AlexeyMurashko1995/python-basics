import asyncio
import httpx


# # ------------------------------------------
# # Task 1
# # ------------------------------------------


# async def send_mail(user: int):
#     print(f'Sending mail to {user}')
#     await asyncio.sleep(2)
#     print(f'Email to {user} was sent')


# async def get_ip():
#     url = 'https://httpbin.org/ip'
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#         return response.json()


# async def run_all():
#     result = await asyncio.gather(
#         send_mail('Alexey'),
#         get_ip()
#     )
#     return result[1]


# result = asyncio.run(run_all())
# print(result)

# ------------------------------------------
# Task 2
# ------------------------------------------


# async def download_file(file_name: str, download_time: int):
#     print(f'Downloading file {file_name}')
#     await asyncio.sleep(download_time)
#     print(f'{file_name} was successfully downloaded in {download_time} sec')


# async def main():
#         result = await asyncio.gather(
#             download_file('report_pdf', 2),
#             download_file('avatar.png', 1),
#             download_file('database.zip', 5)
#         )


# asyncio.run(main())

# ------------------------------------------
# Task 3
# ------------------------------------------


# async def get_status(url: str):
#       async with httpx.AsyncClient() as client:
#             response = await client.get(url)
#             return response.status_code


# async def run_checks():
#     result = await asyncio.gather(
#          get_status('https://httpbin.org/status/200'),
#          get_status('https://httpbin.org/status/404'),
#          get_status('https://httpbin.org/status/500')
#     )
#     print(result)

# asyncio.run(run_checks())


# ------------------------------------------
# Task 4
# ------------------------------------------

# async def fetch_data(endpoint: str):
#     async with httpx.AsyncClient() as client:
#         url = f'https://httpbin.org/{endpoint}'
#         response = await client.get(url)
#         data = response.json()
#         return data


# async def main():
#     result = await asyncio.gather(
#         fetch_data('user-agent'),
#         fetch_data('headers')
#     )
#     print(result)

# asyncio.run(main())


# ------------------------------------------
# Task 5
# ------------------------------------------


# async def process_order(order_id: int, seconds: int):
#     print(f'Order {order_id} has been sent for processing')
#     await asyncio.sleep(seconds)
#     return f'Order {order_id} has been successfully processed'


# async def start_system():
#     result = await asyncio.gather(
#         process_order(101, 3),
#         process_order(102, 1),
#         process_order(103, 2)
#     )
#     print(result)


# asyncio.run(start_system())

# ------------------------------------------
# Task 6
# ------------------------------------------

# async def process_contract(courier_name: str, delay: int):
#     print(f'[Start] Courier {courier_name} has started the registration process')
#     await asyncio.sleep(delay)
#     print(f'[Done] Courier {courier_name} has signed the contract')


# async def main():
#     result = await asyncio.gather(
#         process_contract('Max', 3),
#         process_contract('Yan', 1),
#         process_contract('Tomasz', 1)
#     )
#     return result


# asyncio.run(main())


# ------------------------------------------
# Task 7
# ------------------------------------------


async def courier_process(courier_name: str, semaphore):
    async with semaphore:
        print(f'[Start] {courier_name}')
        await asyncio.sleep(2)
        print(f'[Finish] {courier_name}')


async def main():
    semaphore = asyncio.Semaphore(2)
    result = await asyncio.gather(
        courier_process('Courier 1', semaphore),
        courier_process('Courier 2', semaphore),
        courier_process('Courier 3', semaphore),
        courier_process('Courier 4', semaphore),
        courier_process('Courier 5', semaphore)
    )
    return result


asyncio.run(main())