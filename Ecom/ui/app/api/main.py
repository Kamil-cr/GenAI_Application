from fastapi import FastAPI, Depends, HTTPException, status, Body, Cookie
from sqlmodel import select, Session
from typing import List, Annotated, Optional
from app.api.utils.settings import REFRESH_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import timedelta
from app.api.utils.services import get_user_by_username, verify_password, create_access_token, signup_user
from app.api.utils.models import Product, TokenData, Token, Cart, Order, User
from app.api.utils.db import lifespan, db_session
from app.api.utils.validation import UserCreate, Cartcreate
from jose import jwt, JWTError
from fastapi.middleware.cors import CORSMiddleware

SECRET_KEY = str(SECRET_KEY)
ALGORITHM = ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/oauth/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI(title="E-commerce API", version="0.1.0", lifespan=lifespan)

origins = [
       "http://localhost:3000",  # Add your Next.js app URL here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[Session, Depends(db_session)]):
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

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/oauth/login", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(db_session)]) -> Token:
    user: User = get_user_by_username(db, form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = create_access_token(
        data={"sub": user.username}, expires_delta=refresh_token_expires
    )
    Cookie(refresh_token, token=refresh_token, httponly=True, max_age=60*60*24*7, expires=60*60*24*7, path="/api/oauth/login")
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@app.post("/api/signup", response_model=User)
async def signup(db: Annotated[Session, Depends(db_session)], user: UserCreate = Body()):
    try:
        return signup_user(user, db)
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))

@app.get("/api/products", response_model=List[Product])
def get_products(session: Annotated[Session, Depends(db_session)]) -> List[Product]:
    products = session.exec(select(Product)).all()
    return products

@app.get("/cart", response_model=List[Cart])
def get_cart(session: Annotated[Session, Depends(db_session)], user: Annotated[User, Depends(get_current_user)]) -> List[Cart]:
    user = session.exec(select(User).filter(User.username == user.username)).first()
    cart = session.exec(select(Cart).filter(Cart.user_id == user.id)).all()
    return cart

@app.post("/cart", response_model=Cart)
def post_cart(cart: Cartcreate, session: Annotated[Session, Depends(db_session)], person: Annotated[User, Depends(get_current_user)]):
    user = session.exec(select(User)).where(User.username == person.username).first()
    cart = Cart(**cart.model_dump(), user_id=user.id)
    session.add(cart)
    session.commit()
    session.refresh()
    return {"message": "Successful"}

@app.post("/order", response_model=Order)
def post_order(order: Order, session: Annotated[Session, Depends(db_session)]):
    session.add(order)
    session.commit()
    session.refresh()
    return {"message": "Successful"}

@app.get("/orders", response_model=List[Order])
def get_orders(session: Annotated[Session, Depends(db_session)]):
    orders = session.exec(select(Order)).all()
    return orders