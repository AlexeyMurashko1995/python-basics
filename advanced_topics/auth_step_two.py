from fastapi import FastAPI
import jwt

app = FastAPI()

SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'


def create_token(user_id: int):
    payload = {'sub': str(user_id)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return int(payload['sub'])

