from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Task

app = FastAPI(title="Task API", version="1.0")

# ---------- Create tables on startup ----------
Base.metadata.create_all(bind=engine)


# ---------- Request body models ----------
class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


# ---------- Stage 1: root and health ----------
@app.get("/")
def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}


@app.get("/health")
def health():
    return {"status": "ok"}


# ---------- Stage 2: read ----------
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


# ---------- Stage 3: create ----------
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    if not task.title or not task.title.strip():
        raise HTTPException(status_code=400, detail="Title is required")

    new_task = Task(title=task.title, done=False)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# ---------- Stage 4: update & delete ----------
@app.put("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

    if update.title is not None:
        if not update.title.strip():
            raise HTTPException(status_code=400, detail="Title cannot be empty")
        task.title = update.title

    if update.done is not None:
        task.done = update.done

    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

    db.delete(task)
    db.commit()
    return