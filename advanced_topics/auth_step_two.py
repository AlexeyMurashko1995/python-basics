from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'


def create_token(user_id: int):
    payload = {'sub': str(user_id)}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_id(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id = payload['sub']
    return int(user_id)


@app.post('/login')
def login(user_id: int):
    token = create_token(user_id)
    return {'access': token}


@app.get('/profile')
def profile(user_id: int = Depends(verify_id)):
    return {'user_id': user_id}