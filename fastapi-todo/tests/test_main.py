from fastapi.testclient import TestClient   
from fastapi_todo.main import app, Todo, db_session
from sqlmodel import Session, create_engine, SQLModel, select
from fastapi_todo import settings

def test_read_main():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_todos():
    client = TestClient(app=app)
    connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)
    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        app.dependency_overrides[db_session] = get_session_override 

        response = client.get("/todos")
        assert response.status_code == 200
        assert session.exec(select(Todo)).all()

def test_post_todos():
    client = TestClient(app=app)
    connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)
    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        app.dependency_overrides[db_session] = get_session_override 

        response = client.post("/todos/?todo=Test")
        assert response.status_code == 200


def test_patch_todos():
    client = TestClient(app=app)
    connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)
    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        app.dependency_overrides[db_session] = get_session_override 

        response = client.patch("/todos/?id=3&update_todo=Test")
        assert response.status_code == 200

def test_delete_todos():
    client = TestClient(app=app)
    connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)
    engine = create_engine(
        connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        app.dependency_overrides[db_session] = get_session_override 

        response = client.delete("/todos/?id=3")
        assert response.status_code == 200

