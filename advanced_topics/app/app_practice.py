import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import bcrypt
import jwt
import asyncio
from pydantic import BaseModel
import httpx
from sqlmodel import SQLModel, Session, select
from app.database import engine, get_session
from app.models import User
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

load_dotenv()

app = FastAPI(lifespan=lifespan)


def get_hash_password(password: str):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_bytes = bcrypt.hashpw(password_bytes, salt)
    hash_string = hash_bytes.decode('utf-8')
    return hash_string


def verify_password(hash_string: str, password: str):
    password_bytes = password.encode('utf-8')
    hash_bytes = hash_string.encode('utf-8')
    comparison = bcrypt.checkpw(password_bytes, hash_bytes)
    return comparison


SECRET_KEY = os.getenv('SECRET_KEY', default='fallback_secret_key')
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

class AIRequest(BaseModel):
    prompt: str


def create_token(user_id: int):
    payload = {'sub': str(user_id)}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


async def simulate_ai_model(prompt: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post('https://httpbin.org/post',
            headers={'Authorization': f'Bearer {os.getenv('AI_API_KEY')}'},
            json={'model': 'gpt-40', 'user_prompt': prompt},
            timeout=5.0)
            response = response.json()
            clean_prompt = response['json']['user_prompt']
            return f'AI response to {clean_prompt}'
    except httpx.HTTPError:
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, detail='AI Service is currently unavailable. Try again later.')


def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload['sub']
        query = select(User).where(User.id == int(user_id))
        result = session.exec(query)
        user = result.first()
        if not user:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='User not found')
        return user.username
    except jwt.PyJWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')


@app.post('/tg-ai/generate')
async def generate_text(request_data: AIRequest, username: str = Depends(get_current_user)):
    response = await simulate_ai_model(request_data.prompt)
    return {'status': 'success', 'username': username, 'result': response}


@app.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    query = select(User).where(User.username == form_data.username)
    result = session.exec(query)
    user = result.first()
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='User not found')
    else:
        user_hash = user.hashed_password
        result = verify_password(user_hash, form_data.password)
        if not result:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
        token = create_token(user.id)
        return {'access_token': token, 'token_type': 'bearer'}


@app.get('/users/me')
def profile(username: str = Depends(get_current_user)):
    return {'current_username': username}



