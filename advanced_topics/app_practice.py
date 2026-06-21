from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import bcrypt
import jwt
import asyncio
from pydantic import BaseModel
import httpx


app = FastAPI()


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


SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'

USERS_DB = {'alex': {'id': 1, 'password': get_hash_password('Alex123')}}

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
            headers={'Authorization': 'Bearer fake-ai-key-999'},
            json={'model': 'gpt-40', 'user_prompt': prompt},
            timeout=5.0)
            response = response.json()
            clean_prompt = response['json']['user_prompt']
            return f'AI response to {clean_prompt}'
    except httpx.HTTPError:
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, detail='AI Service is currently unavailable. Try again later.')


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload['sub']
        for username, id_user in USERS_DB.items():
            if int(user_id) == id_user['id']:
                return username
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='User not found')
    except jwt.PyJWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')


@app.post('/tg-ai/generate')
async def generate_text(request_data: AIRequest, username: str = Depends(get_current_user)):
    response = await simulate_ai_model(request_data.prompt)
    return {'status': 'success', 'username': username, 'result': response}


@app.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username not in USERS_DB:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    user = USERS_DB[form_data.username]
    user_hash = user['password']
    result = verify_password(user_hash, form_data.password)
    if not result:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    else:
        token = create_token(user['id'])
        return {'access_token': token, 'token_type': 'bearer'}


@app.get('/users/me')
def profile(username: str = Depends(get_current_user)):
    return {'current_username': username}

