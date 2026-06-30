from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
import httpx

from app.core.database import engine
from app.routers.auth import router as auth_router
from app.routers.products import router as products_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    app.state.ai_model_name = 'GPT-4o-mini'
    app.state.http_client = httpx.AsyncClient()
    yield
    await app.state.http_client.aclose()

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)

app.include_router(products_router)