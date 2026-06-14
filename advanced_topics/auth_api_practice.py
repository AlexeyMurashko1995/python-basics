from fastapi import FastAPI, Depends
import jwt

app = FastAPI()

SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'


def create_token(user_id: int):
    payload = {'sub': str(user_id)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_id(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return int(payload['sub'])


@app.post('/login')
def login(user_id: int):
    token = create_token(user_id)
    return {'access token': token}


@app.get('/profile')
def get_profile(user_id: int = Depends(verify_id)):
    return {'message': f'Hi, user {user_id}'}