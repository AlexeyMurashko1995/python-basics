from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
import bcrypt


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def get_password_hash(password: str):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_bytes = bcrypt.hashpw(password_bytes, salt)
    hash_string = hash_bytes.decode('utf-8')
    return hash_string


def verify_password(password: str, hash_string: str):
    password_bytes = password.encode('utf-8')
    hash_bytes = hash_string.encode('utf-8')
    comparison = bcrypt.checkpw(password_bytes, hash_bytes)
    return comparison


SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'

USERS_DB = {'alex':{'id': 1, 'password': get_password_hash('Alex123')}}


def create_token(user_id: int):
    payload = {'sub': str(user_id)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return int(payload['sub'])


@app.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = create_token(form_data)
    return {'access': token}


@app.get('/profile')
def profile(user_id: int = Depends(verify_token)):
    return {'user_id': user_id}

