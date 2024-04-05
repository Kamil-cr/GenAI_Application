from uuid import uuid4
from fastapi import FastAPI, Depends, HTTPException, status, Body
from sqlmodel import select, Session
from typing import List, Annotated, Optional
from app.api.utils.settings import REFRESH_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import timedelta
from app.api.utils.services import get_current_user, get_user_by_username, verify_password, create_access_token, signup_user
from app.api.utils.models import Cart, CartCreate, Product, TokenData, Token, Order, User, UserCreate, Userlogin
from app.api.utils.db import lifespan, db_session
from fastapi.middleware.cors import CORSMiddleware

SECRET_KEY = str(SECRET_KEY)
ALGORITHM = ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI(title="E-commerce API", version="0.1.0", lifespan=lifespan)

origins = [
    "http://localhost:3000",  # Add your Next.js app URL here
    "http://localhost:3001",  # Add your FastAPI app URL here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/login", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(db_session)]) -> Token:
    user: Userlogin = get_user_by_username(db, form_data.username)
    # user = user.model_validate(User)
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
    return {"access_token": access_token, "refresh_token": refresh_token, "expires_in": access_token_expires+refresh_token_expires, "token_type": "bearer"}

@app.post("/api/signup", response_model=User)
async def signup(db: Annotated[Session, Depends(db_session)], user: UserCreate = Body()):
    try:
        return signup_user(user, db)
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))

@app.get("/api/users/me", response_model=User)
async def read_users_me(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[Session, Depends(db_session)]) -> User:
    user = await get_current_user(token, db)
    return user

@app.get("/api/products", response_model=List[Product])
def get_products(session: Annotated[Session, Depends(db_session)], query: Optional[str] = None) -> List[Product]:
    if query:
        products = session.exec(select(Product).where(Product.slug.contains(query))).all()
    else:
        products = session.exec(select(Product)).all()
    return products

@app.get("/api/products/{product_slug}", response_model=Product)
def get_product(product_slug: str, session: Annotated[Session, Depends(db_session)]) -> Product:
    product = session.exec(select(Product).filter(Product.slug == product_slug)).first()
    return product

@app.get("/api/cart", response_model=List[Cart])
def get_cart(session: Annotated[Session, Depends(db_session)], user: Annotated[User, Depends(get_current_user)]) -> List[Cart]:
    user = session.exec(select(User).filter(User.username == user.username)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    cart = session.exec(select(Cart).filter(Cart.user_id == user.id)).all()
    return cart

@app.post("/api/cart", response_model=Cart)
def post_cart(cart: CartCreate, session: Annotated[Session, Depends(db_session)], user: Annotated[User, Depends(get_current_user)]) -> Cart:
    user = session.exec(select(User).where(User.username == user.username)).first()
    product = session.exec(select(Product).where(Product.sku == cart.product_id)).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    prod_in_cart = session.exec(select(Cart).where(Cart.product_id == cart.product_id, Cart.user_id == user.id, Cart.product_size == cart.product_size)).first()
    if prod_in_cart:
        prod_in_cart.quantity += cart.quantity
        prod_in_cart.product_total += product.price*cart.quantity
        session.add(prod_in_cart)
        session.commit()
        session.refresh(prod_in_cart)
        return prod_in_cart
    cart = Cart(product_id=cart.product_id, product_total=product.price*cart.quantity, product_size=cart.product_size, quantity=cart.quantity, user_id=user.id)
    session.add(cart)
    session.commit()
    session.refresh(cart)
    return cart


# @app.post("/cart", response_model=Cart)
# def post_cart(cart: Cartcreate, session: Annotated[Session, Depends(db_session)], person: Annotated[User, Depends(get_current_user)]):
#     user = session.exec(select(User)).where(User.username == person.username).first()
#     cart = Cart(**cart.model_dump(), user_id=user.id)
#     session.add(cart)
#     session.commit()
#     session.refresh()
#     return {"message": "Successful"}

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