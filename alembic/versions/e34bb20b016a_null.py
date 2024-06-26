"""null

Revision ID: e34bb20b016a
Revises: c580ac40d15d
Create Date: 2024-06-24 12:51:55.167974

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e34bb20b016a'
down_revision: Union[str, None] = 'c580ac40d15d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('plugin', 'price',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('plugin', 'one_time_price',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('plugin', 'one_time_price',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('plugin', 'price',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
