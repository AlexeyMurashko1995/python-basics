import asyncio
import redis
import time


SIMULATED_REDIS = {}


async def get_article_from_db(article_id: int) -> dict:
    await asyncio.sleep(2)
    return {"id": article_id, "title": f"Article: #{article_id}"}


async def read_article(article_id: int, ttl_seconds: int = 4):
    if article_id in SIMULATED_REDIS and time.time() - SIMULATED_REDIS[article_id]["created_at"] < ttl_seconds:
        return SIMULATED_REDIS[article_id]["data"]
    article = await get_article_from_db(article_id=article_id)
    SIMULATED_REDIS[article_id] = {"data": article, "created_at": time.time()}
    return article