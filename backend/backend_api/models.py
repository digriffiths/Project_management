from sqlalchemy import String, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
    
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


class Task(Base):
    __tablename__ = 'tasks'

    task_id: Mapped[str] = mapped_column(primary_key=True)
    task_name: Mapped[str] = mapped_column(nullable=False, index=True)
    project: Mapped[str] = mapped_column()
    task_status: Mapped[str] = mapped_column(Enum("pending", "complete", name="taskstatus_enum"), nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    task_due_by: Mapped[datetime] = mapped_column()
    user_id: Mapped[str] = mapped_column(String, ForeignKey('users.user_id'))
    is_high_priority: Mapped[bool] = mapped_column()