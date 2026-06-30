from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import SQLModel, Session
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import SQLModel, select
import jwt
import bcrypt

from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRES_MINUTES
from app.core.database import engine, get_session
from app.models.user import User, UserCreate, UserRead

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        target_user = payload['sub']
        if not target_user:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail='User not found')
        query = select(User).where(target_user == User.username)
        result = session.exec(query).first()
        if result:
            return result
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='User not found')
    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')


class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: User = Depends(get_current_user)):
        if current_user.role not in self.allowed_roles:
            raise HTTPException(
                status.HTTP_403_FORBIDDEN,
                detail="You do not have the access"
            )


@router.post('/register')
def register_user(user_data: UserCreate):
    with Session(engine) as session:
        query = select(User).where(User.username == user_data.username)
        result = session.exec(query).first()
        if result:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Username already registered')
        password_bytes = user_data.password.encode('utf-8')
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt)
        hash_string = password_hash.decode('utf-8')
        db_user = User(username=user_data.username, hashed_password=hash_string)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user


@router.post('/login')
def login_user(user_data: UserCreate):
    with Session(engine) as session:
        query = select(User).where(User.username == user_data.username)
        result = session.exec(query).first()
        if not result:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Invalid login or password')
        password_bytes = user_data.password.encode('utf-8')
        hash_bytes = result.hashed_password.encode('utf-8')
        comparison = bcrypt.checkpw(password_bytes, hash_bytes)
        if comparison:
            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
            payload = {'sub': result.username, 'exp': expire}
            token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
            return {'access_token': token, 'token_type': 'bearer'}
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Invalid login or password')


@router.get('/protected', response_model=UserRead)
def get_protected_data(user_data: User = Depends(get_current_user)):
    return user_data