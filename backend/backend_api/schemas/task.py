from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Optional

class TaskStatus(str, Enum):
    pending = "pending"
    complete = "complete"

class TaskIn(BaseModel):
    task_name: str
    project: str
    task_due_by: datetime
    is_high_priority: bool = False

class TaskOut(TaskIn):
    task_id: str
    user_id: str
    task_status: TaskStatus
    created_at: datetime
    
class TaskUpdate(BaseModel):
    task_name: Optional[str] = None
    project: Optional[str] = None
    task_due_by: Optional[datetime] = None
    user_id: Optional[str] = None
    task_status: Optional[TaskStatus] = None
    is_high_priority: Optional[bool] = None