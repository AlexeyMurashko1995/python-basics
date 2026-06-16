from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'


def create_token(user_id: int):
    payload = {'sub': str(user_id)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return int(payload['sub'])


@app.post('/login')
def login(user_id: int):
    token = create_token(user_id)
    return {'access': token}


@app.get('/profile')
def profile(user_id: int = Depends(verify_token)):
    return {'user_id': user_id}

