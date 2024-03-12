from uitclass import main
from sqlmodel import Session, select
from fastapi import Depends
from typing import Annotated


def create_todo(todo: str, session: Session):
        todo = main.Todo(todo=todo)
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo


def read_todos(session: Session):
        todos = session.exec(select(main.Todo)).all()
        return todos

def read_todo(todo_id: int, session: Session):
        todo = session.get(main.Todo, todo_id)
        return todo

def delete_todo(todo_id: int, session: Session):
        todo = session.get(main.Todo, todo_id)
        session.delete(todo)
        session.commit()
        return todo