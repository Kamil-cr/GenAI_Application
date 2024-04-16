from fastapi.testclient import TestClient
from app.api.main import app
from app.api.utils.db import db_session
from app.api.utils import settings
from sqlmodel import create_engine, Session, SQLModel

def test_create_user():
    client = TestClient(app)

    connection_string = str(settings.DATABASE_URL)

    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                yield session  

        app.dependency_overrides[db_session] = get_session_override 

        response = client.post(
            "/api/signup",
            json={
                "username": "testuser1",
                "email": "testuser1@gmail.com",
                "password": "password"
            }
        )
        assert response.status_code == 200
        assert response.json()["username"] == "testuser1"

def test_get_product():
    client = TestClient(app=app)
    connection_string = str(settings.DATABASE_URL)

    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
            yield session  

        app.dependency_overrides[db_session] = get_session_override 

        response = client.get("/api/products")
        assert response.status_code == 200
        assert response.json()[0]["name"] == "SLOGAN PRINT T-SHIRT"