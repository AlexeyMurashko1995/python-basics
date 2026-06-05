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

async def fetch_data(endpoint: str):
    async with httpx.AsyncClient() as client:
        url = f'https://httpbin.org/{endpoint}'
        response = await client.get(url)
        data = response.json()
        return data


async def main():
    result = await asyncio.gather(
        fetch_data('user-agent'),
        fetch_data('headers')
    )
    print(result)

asyncio.run(main())