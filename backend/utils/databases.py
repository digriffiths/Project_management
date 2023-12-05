from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker, declarative_base
import os

from collections.abc import AsyncGenerator

from backend.backend_api import models

Base = declarative_base()

class AsyncSQLDB:
    def __init__(self):
        DATABASE_URL = (
            f'postgresql+asyncpg://{os.getenv("SQLDB_USER")}:{os.getenv("SQLDB_PASS")}'
            f'@{os.getenv("SQLDB_HOST")}:{os.getenv("SQLDB_PORT")}/{os.getenv("SQLDB_NAME")}'
        )

        self.engine = create_async_engine(DATABASE_URL)
        self.Session = async_sessionmaker(self.engine)

    async def get_session(self) -> AsyncGenerator:

        async with self.engine.begin() as conn:
            # Drop all tables
            # await conn.run_sync(models.Base.metadata.drop_all)
            # Create all tables
            await conn.run_sync(models.Base.metadata.create_all)

        db = self.Session()
        try:

            yield db

        except Exception as e:
            print(e)
            raise e
        finally:
            await db.close()
