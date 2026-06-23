from sqlmodel import SQLModel, Field


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(unique=True)
    price: int

