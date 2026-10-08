import pytest
from database import Base, engine, get_db
from httpx import ASGITransport, AsyncClient
from main_2 import app
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


test_engine = create_async_engine("sqlite+aiosqlite:///:memory:")


async def override_get_db():
    session_factory = async_sessionmaker(bind=test_engine, expire_on_commit=False)
    async with session_factory() as fake_session:
        yield fake_session


@pytest.fixture
async def get_client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client


@pytest.fixture(autouse=True, scope="function")
async def setup_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        app.dependency_overrides[get_db] = override_get_db
        yield conn
        await conn.run_sync(Base.metadata.drop_all)
        app.dependency_overrides.clear()
