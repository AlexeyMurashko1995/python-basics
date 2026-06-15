from fastapi import FastAPI, Depends
import jwt


app = FastAPI()

SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'


def create_token(user_id: int):
    payload = {'sub': str(user_id)}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_id(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    id = payload['sub']
    return int(id)

