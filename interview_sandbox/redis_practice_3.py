import asyncio
import time
import redis


SIMULATED_REDIS = {}


async def fetch_article_from_db(article_id: int):
    await asyncio.sleep(2)
    return {"id": article_id, "title": f"Article: #{article_id}"}


async def get_article(article_id: int, ttl_seconds: int = 3):
    if article_id in SIMULATED_REDIS and time.time() - SIMULATED_REDIS[article_id]["created_at"] < ttl_seconds:
        print("CACHE HIT")
        return SIMULATED_REDIS[article_id]["data"]
    print("CACHE MISS")
    article = await fetch_article_from_db(article_id=article_id)
    SIMULATED_REDIS[article_id] = {"data": article, "created_at": time.time()}
    return article


async def main():
    await get_article(1, 3)
    await get_article(1, 3)
    await asyncio.sleep(4)
    await get_article(1, 3)


asyncio.run(main())