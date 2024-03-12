from database import Sessionlocal, engine
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import Todo_APP.crud
import schema
import models

models.Base.metadata.create_all(bind=engine)

app: FastAPI = FastAPI()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos/")
def create_todo(text: schema.TodoCreate, db: Session = Depends(get_db)):
    db_user = Todo_APP.crud.create_todo(db, todo=text)
    return db_user

@app.get("/todos/")
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return Todo_APP.crud.get_todo_by_id(id=todo_id, db=db)

@app.patch("/todos/{todo_id}")
def update_a_todo(todo_id: int, todo_data: schema.TodoUpdate, db: Session = Depends(get_db)):
    updated_todo = Todo_APP.crud.update_todo_by_id(todo_data, todo_id, db)
    return updated_todo

@app.delete("/todos/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    return Todo_APP.crud.delete_todo(id=todo_id, db=db)