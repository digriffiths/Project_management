"""column renamed to project

Revision ID: 8e6ea72d924f
Revises: 
Create Date: 2023-11-23 16:48:43.249614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8e6ea72d924f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('tasks', 'task_description', new_column_name='project')

def downgrade() -> None:
    op.alter_column('tasks', 'project', new_column_name='task_description')