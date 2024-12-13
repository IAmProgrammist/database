"""empty message

Revision ID: 304d95d2ddc4
Revises: 5fe2eeb027e0
Create Date: 2024-12-13 13:03:37.015020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '304d95d2ddc4'
down_revision: Union[str, None] = '5fe2eeb027e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_task_until_date'), 'task', ['until_date'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_until_date'), table_name='task')
    # ### end Alembic commands ###
