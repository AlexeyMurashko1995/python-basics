import jwt

SECRET_KEY = 'my_secret_key'
ALGORITHM = 'HS256'


def create_token(user_id: int):
    payload = {'sub': str(user_id)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)