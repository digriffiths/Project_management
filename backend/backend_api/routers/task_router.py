
from fastapi import APIRouter, Request, Depends, HTTPException
from backend.backend_api.schemas.task import TaskIn, TaskOut, TaskUpdate
from backend.utils.databases import AsyncSQLDB
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
from backend.backend_api import security
from backend.backend_api.models import Task
from backend.backend_api.services import task_service
from typing import List, Any

router = APIRouter()
async_db = AsyncSQLDB()

@router.post("/add_task")
async def add_task(request: Request, task_in: TaskIn, db: AsyncSession = Depends(async_db.get_session)) -> TaskOut:
    token = request.headers['authorization']
    user_id = security.verify_access_token(token)
    task = Task(task_id = str(uuid.uuid4()),
                task_status = "pending",
                user_id = user_id,
                **task_in.model_dump(),
                )
    task = await task_service.add_task(db, task)

    return task


@router.get("/user_tasks")
async def get_tasks(request: Request, db: AsyncSession = Depends(async_db.get_session)) -> List[TaskOut] | Any:
    token = request.headers['authorization']
    user_id = security.verify_access_token(token)
    tasks = await task_service.get_tasks(db, user_id)    
    task_list = []
    for task in tasks:
        task_schema = TaskOut(
            task_id=task.task_id,
            user_id=task.user_id,
            task_status=task.task_status,
            task_name=task.task_name,
            project=task.project,
            task_due_by=task.task_due_by,
            created_at=task.created_at,
            is_high_priority=task.is_high_priority
        )
        task_list.append(task_schema)

    # Sort the task list so that high priority tasks come first
    task_list = sorted(task_list, key=lambda task: not task.is_high_priority)

    return task_list

@router.put("/update_task/{task_id}")
async def update_task(task_id: str, request: Request, task_update: TaskUpdate, db: AsyncSession = Depends(async_db.get_session)) -> TaskOut:
    token = request.headers['authorization']
    token_user_id = security.verify_access_token(token)
    task = await task_service.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=400, detail="Invalid task id")

    if task.user_id != token_user_id:
        raise HTTPException(status_code=400, detail="Invalid token")

    task = await task_service.update_task(db, task, task_update)
    return TaskOut(
        task_id=task.task_id,
        user_id=task.user_id,
        task_status=task.task_status,
        task_name=task.task_name,
        project=task.project,
        task_due_by=task.task_due_by,
        created_at=task.created_at,
        is_high_priority=task.is_high_priority
    )

@router.delete("/delete_task/{task_id}")
async def delete_task(task_id: str, request: Request, db: AsyncSession = Depends(async_db.get_session)):
    token = request.headers['authorization']
    token_user_id = security.verify_access_token(token)
    task = await task_service.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=400, detail="Invalid task id")

    if task.user_id != token_user_id:
        raise HTTPException(status_code=400, detail="Invalid token")

    task_to_delete = TaskOut(
        task_id=task.task_id,
        user_id=task.user_id,
        task_status=task.task_status,
        task_name=task.task_name,
        project=task.project,
        task_due_by=task.task_due_by,
        created_at=task.created_at,
        is_high_priority=task.is_high_priority
    )
    await task_service.delete_task(db, task)
    return {"message": "Task deleted successfully", "task": task_to_delete.model_dump()}
