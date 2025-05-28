from enum import Enum
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus | None = TaskStatus.pending


class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass


class TaskInDB(TaskBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }