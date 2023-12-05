"""add column is high priority

Revision ID: 8e16a92e9210
Revises: 8e6ea72d924f
Create Date: 2023-11-26 11:28:24.989402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8e16a92e9210'
down_revision: Union[str, None] = '8e6ea72d924f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('is_high_priority', sa.Boolean()))


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'is_high_priority')
