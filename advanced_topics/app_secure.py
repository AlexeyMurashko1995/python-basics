from fastapi import FastAPI, Depends, HTTPException, status
import bcrypt
import jwt
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer


app = FastAPI()


def get_hash_password(password: str):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_bytes = bcrypt.hashpw(password_bytes, salt)
    hash_string = hash_bytes.decode('utf-8')
    return hash_string


def verify_password(hash_string: str, password:str):
    hash_bytes = hash_string.encode('utf-8')
    password_bytes = password.encode('utf-8')
    comparison = bcrypt.checkpw(password_bytes, hash_bytes)
    return comparison


USERS_DB = {'alex':{'id': 1, 'password': get_hash_password('Alex123')}}

SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def create_token(user_id: int):
    payload = {'sub': str(user_id)}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


@app.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username not in USERS_DB:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    else:
        user = USERS_DB[form_data.username]
        user_hash = user['password']
        result = verify_password(user_hash, form_data.password)
        if not result:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
        token = create_token(user['id'])
        return {'access_token': token, 'token_type': 'bearer'}
