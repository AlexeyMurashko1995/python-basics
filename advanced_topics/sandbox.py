from sqlmodel import SQLModel, Field, create_engine
from pydantic import BaseModel


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(unique=True)
    price: int

class ProductCreate(BaseModel):
    title: str
    price: int


filename = 'sandbox.db'
url = f'sqlite:///{filename}'

engine = create_engine(url)