import asyncio
import redis
import time


SIMULATED_REDIS = {}


async def get_article_from_db(article_id: int) -> dict:
    await asyncio.sleep(2)
    return {"id": article_id, "title": f"Article: #{article_id}"}


async def read_article(article_id: int, ttl_seconds: int = 4):
    if article_id in SIMULATED_REDIS and time.time() - SIMULATED_REDIS[article_id]["created_at"] < ttl_seconds:
        print("CACHE HIT")
        return SIMULATED_REDIS[article_id]["data"]
    print("CACHE MISS")
    article = await get_article_from_db(article_id=article_id)
    SIMULATED_REDIS[article_id] = {"data": article, "created_at": time.time()}
    return article


async def update_article_in_db(article_id: int, new_title: str):
    await asyncio.sleep(1)
    if article_id in SIMULATED_REDIS:
        del SIMULATED_REDIS[article_id]
    return {"id": article_id, "title": new_title}


async def main():
    await read_article(1)
    await read_article(1)
    await update_article_in_db(1, "New Python Tricks")
    await read_article(1)


asyncio.run(main())