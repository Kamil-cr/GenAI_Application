from sqlalchemy.orm import Session
from models import Todo
import schema

def create_todo(db: Session, todo: schema.TodoCreate):
    db_todo = Todo(text=todo.text)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return "todo created successfully...."

def get_all(db: Session):
    return db.query(Todo).all()

def get_todo_by_id(id: int, db: Session):
    return db.query(Todo).filter(Todo.id == id).first()

def update_todo_by_id(todo_data: schema.TodoUpdate,id: int, db: Session):
    todo = db.query(Todo).filter(Todo.id == id).first()
    todo.text = todo_data.text
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(id: int, db: Session):
    db_todo = db.query(Todo).filter(Todo.id == id).first()
    db.delete(db_todo)
    db.commit()
    return "todo deleted successfully...."