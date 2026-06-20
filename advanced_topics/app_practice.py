from fastapi import FastAPI
import bcrypt


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

USERS_DB = {'alex':{'id': 1, 'password': get_hash_password('Alex123')}}