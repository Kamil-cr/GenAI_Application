from fastapi.testclient import TestClient
from api.main import app
from utils.db import db_session
from utils.models import User
from utils import settings
from sqlmodel import create_engine, Session, SQLModel

def test_get_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# def test_create_user():
#     client = TestClient(app)

#     connection_string = str(settings.TEST_DATABASE_URL)

#     engine = create_engine(
#         connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

#     SQLModel.metadata.create_all(engine)  

#     with Session(engine) as session:  

#         def get_session_override():  
#                 yield session  

#         app.dependency_overrides[db_session] = get_session_override 

#         response = client.post(
#             "/signup",
#             json={
#                 "id": "123e4567-e89b-12d3-a456-426755440000",
#                 "username": "testuser1",
#                 "email": "testuser1@gmail.com",
#                 "password": "password"
#             }
#         )
#         assert response.status_code == 200
#         assert response.json()["username"] == "testuser1"

def test_create_product():
    client = TestClient(app)
    connection_string = str(settings.TEST_DATABASE_URL)

    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                yield session  

        app.dependency_overrides[db_session] = get_session_override 
        response = client.post(
            "/product",
            json={
                "sku": "123e4567-e89b-12d3-a456-426755440000",
                "name": "Test Product",
                "description": "This is a test product",
                "price": 10.0,
                "slug": "test-product",
                "quantity": 10,
                "size": "M"
            },
        )
        assert response.status_code == 200
        assert response.json()["name"] == "Test Product"