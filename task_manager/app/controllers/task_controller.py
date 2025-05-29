from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from uuid import UUID
from typing import Optional
from ..database import get_db
from ..schemas.task_schema import TaskCreate, TaskUpdate, TaskInDB, TaskStatus
from ..crud.task_crud import create_task, get_task, get_tasks, update_task, delete_task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskInDB)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)
    
@router.get("/", response_model=list[TaskInDB])
def read_all(
    skip: int = 0,
    limit: int = 100,
    status: Optional[TaskStatus] = Query(None),
    db: Session = Depends(get_db)):
    return get_tasks(db, skip, limit, status=status)


@router.get("/{task_id}", response_model=TaskInDB)
def read(task_id: UUID, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskInDB)
def update(task_id: UUID, task: TaskUpdate, db: Session = Depends(get_db)):
    updated = update_task(db, task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@router.delete("/{task_id}", response_model=TaskInDB)
def delete(task_id: UUID, db: Session = Depends(get_db)):
    deleted = delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted