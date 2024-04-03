from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from app.api.utils.db import db_session
from app.api.utils.settings import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES, JWT_REFRESH_SECRET_KEY
from app.api.utils.models import TokenData, User, UserCreate
from datetime import datetime, timedelta, timezone
from sqlmodel import Session, select
from fastapi import Depends, HTTPException, status
from pydantic import EmailStr
from uuid import uuid4
from typing import Annotated, Union, Any

SECRET_KEY = str(SECRET_KEY)
ALGORITHM = str(ALGORITHM)
ACCESS_TOKEN_EXPIRE_MINUTES = ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_MINUTES = REFRESH_TOKEN_EXPIRE_MINUTES
JWT_REFRESH_SECRET_KEY = str(JWT_REFRESH_SECRET_KEY)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user_by_username(db:Session,username:str) -> User:
    if username is None:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,headers={"WWW-Authenticate": 'Bearer'},detail={"error": "invalid_token", "error_description": "The access token expired"})

    user = db.exec(select(User).filter(User.username == username)).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user

def get_user_by_id(db: Session, userid: int) -> User:
    if userid is None:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             headers={"WWW-Authenticate": 'Bearer'},
                             detail={"error": "invalid_token", "error_description": "The access token expired"})
    user = db.get(User, userid)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    
    return user
    
def get_user_by_email(db:Session,user_email: EmailStr) -> User:
    if user_email is None:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,headers={"WWW-Authenticate": 'Bearer'},detail={"error": "invalid_token", "error_description": "The access token expired"})

    user = db.get(User, user_email)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user

def authenticate_user(db, username: str, password: str) -> User:
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(data)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def signup_user(user: UserCreate, db: Session) -> User:
    search_user_by_email = db.exec(select(User).filter(User.email == user.email)).first()
    if search_user_by_email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Email id already registered")
    
    search_user_by_username = db.exec(select(User).filter(User.username == user.username)).first()
    if search_user_by_username:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Try Different username")
    
    hashed_password = get_password_hash(user.hashed_password)

    new_user = User(id = uuid4(),username=user.username, email=user.email, hashed_password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[Session, Depends(db_session)]) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user