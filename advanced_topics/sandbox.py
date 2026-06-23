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


@app.get('/products')
def read_products():
    with Session(engine) as session:
        query = select(Product)
        result = session.exec(query)
        all_products = result.all()
        return all_products


@app.get('/products/{product_id}')
def read_product_by_id(product_id: int):
    with Session(engine) as session:
        query = select(Product).where(Product.id==product_id)
        result = session.exec(query)
        product_by_id = result.first()
        if product_by_id:
            return product_by_id
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Product not found')


@app.delete('/products/{product_id}')
def delete_product_by_id(product_id: int):
    with Session(engine) as session:
        query = select(Product).where(Product.id==product_id)
        result = session.exec(query)
        target_product = result.first()
        if not target_product:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Product not found')
        session.delete(target_product)
        session.commit()
        return {'status': 'success', 'message': 'Product deleted'}


@app.put('/products/{product_id}')
def update_product(product_id: int, product_data: ProductCreate):
    with Session(engine) as session:
        query = select(Product).where(Product.id==product_id)
        result = session.exec(query)
        target_product = result.first()
        if not target_product:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Product not found')
        target_product.title = product_data.title
        target_product.price = product_data.price
        session.commit()
        session.refresh(target_product)
        return target_product