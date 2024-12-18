"""empty message

Revision ID: a7ecf56d944e
Revises: 719c5df6242a
Create Date: 2024-12-05 15:14:49.752816

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7ecf56d944e'
down_revision: Union[str, None] = '719c5df6242a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contract', 'payment')
    op.add_column('payment', sa.Column('energy_source', sa.String(), server_default='Undefined', nullable=False))
    op.add_column('payment', sa.Column('payment', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('payment', 'payment')
    op.drop_column('payment', 'energy_source')
    op.add_column('contract', sa.Column('payment', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
