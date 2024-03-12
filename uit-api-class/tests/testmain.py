from fastapi.testclient import TestClient
from uitclass.main import app
from sqlmodel import create_engine, SQLModel, Session
from uitclass.main import db_session

def test_read_main():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

# def test_create_todo():
#     client = TestClient(app=app)
#     connection_string = str("postgresql://kamilzafar54:")

#     engine = create_engine(
#         connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

#     SQLModel.metadata.create_all(engine)  

#     with Session(engine) as session:  

#         def get_session_override():  
#                 return session  

#         app.dependency_overrides[db_session] = get_session_override 

#         response = client.post("/todos?todo=hello")
#         assert response.status_code == 200
#         assert response.json() == {"id": 1, "todo": "hello"}