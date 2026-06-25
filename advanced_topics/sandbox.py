from sqlmodel import SQLModel, Field, create_engine, Session, select
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from contextlib import asynccontextmanager
import bcrypt
import jwt
from datetime import datetime, timedelta, timezone


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str

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

SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'

ACCESS_TOKEN_EXPIRES_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)


@app.post('/product')
def create_product(product: ProductCreate, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
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


@app.post('/register')
def register_user(user_data: UserCreate):
    with Session(engine) as session:
        query = select(User).where(User.username == user_data.username)
        result = session.exec(query).first()
        if result:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Username already registered')
        password_bytes = user_data.password.encode('utf-8')
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt)
        hash_string = password_hash.decode('utf-8')
        db_user = User(username=user_data.username, hashed_password=hash_string)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user


@app.post('/login')
def login_user(user_data: UserCreate):
    with Session(engine) as session:
        query = select(User).where(User.username==user_data.username)
        result = session.exec(query).first()
        if not result:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Invalid login or password')
        password_bytes = user_data.password.encode('utf-8')
        hash_bytes = result.hashed_password.encode('utf-8')
        comparison = bcrypt.checkpw(password_bytes, hash_bytes)
        if comparison:
            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
            payload = {'sub': result.username, 'exp': expire}
            token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
            return {'access_token': token, 'token_type': 'bearer'}
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Invalid login or password')


def get_session():
    with Session(engine) as session:
        yield session


def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        target_user = payload['sub']
        if not target_user:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail='User not found')
        query = select(User).where(target_user == User.username)
        result = session.exec(query).first()
        if result:
            return result
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='User not found')
    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')


@app.get('/protected', response_model=UserRead)
def get_protected_data(user_data: User = Depends(get_current_user)):
    return user_data


