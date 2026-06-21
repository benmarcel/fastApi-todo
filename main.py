from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

class TodoBase(BaseModel):
    title: str
    description: str
    status: Literal["pending", "in-progress", "completed"]

class Todo(TodoBase):
    id: int


todos = [
    Todo(
        id=1,
        title="Learn FastAPI Basics",
        description="Understand how routing and path parameters work.",
        status="in-progress"
    ),
    Todo(
        id=2,
        title="Set up Python Environment",
        description="Install fastapi and uvicorn using pip.",
        status="completed"
    ),
    Todo(
        id=3,
        title="Build CRUD Endpoints",
        description="Write the logic for GET, POST, PUT, and DELETE.",
        status="pending"
    )
]
app = FastAPI()

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{id}")
def get_todo_by_id(id:int):
    for todo in todos:
        if todo.id == id:
            return todo
    return {"message": "Todo not found"}

@app.post("/todos")
def create_todo(newtodo: TodoBase):
    new_id = max(todo.id for todo in todos) + 1 if todos else 1
    new_todo = Todo(id=new_id, **newtodo.model_dump())
    todos.append(new_todo)
    return new_todo

@app.put("/todos/{id}")
def update_todo(id:int, todo_update: TodoBase):
    for todo in todos:
         if todo.id == id:
            todo.title = todo_update.title
            todo.description = todo_update.description
            todo.status = todo_update.status
            return todo
    return {"message": "Todo not found"}

@app.delete("/todos/{id}")
def delete_todo(id:int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}