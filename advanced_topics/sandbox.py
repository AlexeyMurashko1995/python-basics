from sqlmodel import SQLModel, Field, create_engine, Session, select
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager


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

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)


@app.post('/product')
def create_product(product: ProductCreate):
    with Session(engine) as session:
        query = select(Product).where(Product.title == product.title)
        result = session.exec(query)
        target_product = result.first()
        if target_product:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Bad Request')
        else:
            new_product = Product(title=product.title, price=product.price)
            session.add(new_product)
            session.commit()
            session.refresh(new_product)
            return new_product





