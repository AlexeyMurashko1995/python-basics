from fastapi import FastAPI, Depends
from pydantic import BaseModel, ConfigDict
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from models import Item, Category


app = FastAPI()


class ItemCreate(BaseModel):
    title: str
    price: float


class ItemResponse(BaseModel):
    id: int
    title: str
    price: float

    model_config = ConfigDict(from_attributes=True)


class CategoryCreate(BaseModel):
    name: str
    budget_limit: float


class CategoryResponse(BaseModel):
    id: int
    name: str
    budget_limit: float

    model_config = ConfigDict(from_attributes=True)


@app.post("/api/v1/categories", response_model=CategoryResponse)
async def add_category(category_data: CategoryCreate, session: AsyncSession = Depends(get_db)):
    new_category = Category(name=category_data.name, budget_limit=category_data.budget_limit)
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return new_category


@app.post("/api/v1/items", response_model=ItemResponse)
async def add_item(item_data: ItemCreate, session: AsyncSession = Depends(get_db)):
    new_item = Item(title=item_data.title, price=item_data.price)
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item