from sqlalchemy.ext.asyncio import AsyncSession
from backend.backend_api import models
from sqlalchemy import select, delete
from backend.backend_api.schemas.task import TaskUpdate

async def add_task(db: AsyncSession, task: models.Task):
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def get_tasks(db: AsyncSession, user_id: str):
    sql_statement = select(models.Task).where(models.Task.user_id == user_id)
    result = await db.execute(sql_statement)
    all_results = result.scalars().all()
    return all_results

async def get_task(db: AsyncSession, task_id: str):
    sql_statement = select(models.Task).where(models.Task.task_id == task_id)
    result = await db.execute(sql_statement)
    task = result.scalars().one_or_none()
    return task

async def update_task(db: AsyncSession, task: models.Task, new_data: TaskUpdate):

    for key, value in new_data.dict().items():
        if value is not None:
            setattr(task, key, value)

    await db.commit()
    await db.refresh(task)

    return task


async def delete_task(db: AsyncSession, task: models.Task):
    sql_statement = delete(models.Task).where(models.Task.task_id == task.task_id)
    await db.execute(sql_statement)
    await db.commit()