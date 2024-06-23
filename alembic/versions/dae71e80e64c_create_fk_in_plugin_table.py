"""create fk in plugin table

Revision ID: dae71e80e64c
Revises: 2aa2a5ed8a3b
Create Date: 2024-06-22 00:16:15.490538

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dae71e80e64c'
down_revision: Union[str, None] = '2aa2a5ed8a3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'plugin',
        sa.Column('author_id', sa.Integer, sa.ForeignKey('author.id'))
    )


def downgrade() -> None:
    op.drop_column('plugin', 'author_id')

