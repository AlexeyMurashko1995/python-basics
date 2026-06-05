import asyncio
import httpx


# ------------------------------------------
# Task 1
# ------------------------------------------


async def send_mail(user: int):
    print(f'Sending mail to {user}')
    await asyncio.sleep(2)
    print(f'Email to {user} was sent')


async def get_ip():
    url = 'https://httpbin.org/ip'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


async def run_all():
    result = await asyncio.gather(
        send_mail('Alexey'),
        get_ip()
    )
    return result[1]


result = asyncio.run(run_all())
print(result)
