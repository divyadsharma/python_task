from sqlalchemy.orm import Session
from uuid import UUID
from ..models.task import Task
from ..schemas.task_schema import TaskCreate, TaskUpdate, TaskStatus
def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: UUID):
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100, status: TaskStatus = None):
    query = db.query(Task)
    if status:
        query = query.filter(Task.status == status)
    return query.offset(skip).limit(limit).all()

def update_task(db: Session, task_id: UUID, task: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        for key, value in task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)

    return db_task

def delete_task(db: Session, task_id: UUID):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task
