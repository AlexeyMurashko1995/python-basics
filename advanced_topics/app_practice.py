from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import bcrypt
import jwt
import asyncio
from pydantic import BaseModel


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
    await asyncio.sleep(2)
    return f'AI response to: {prompt}'


@app.post('/tg-ai/generate')
async def generate_text(request_data: AIRequest, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload['sub']
        response = await simulate_ai_model(request_data.prompt)
        return {'status': 'success', 'user_id': user_id, 'result': response}
    except jwt.PyJWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')


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
def profile(token: str = Depends(oauth2_scheme)):
    if token:
        return {'caught_token': token}

