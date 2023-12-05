from sqlalchemy.ext.asyncio import AsyncSession
from backend.backend_api import models
from sqlalchemy import select

async def add_user(db: AsyncSession, task: models.User):
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def get_user_by_username(db: AsyncSession, username: str):
    sql_stmt = select(models.User).where(models.User.username == username)
    result = await db.execute(sql_stmt)
    db_user = result.scalars().one_or_none()
    return db_user
