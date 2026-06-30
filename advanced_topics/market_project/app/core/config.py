import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRES_MINUTES = 30