"""create author table

Revision ID: 2aa2a5ed8a3b
Revises: 3d73795bf6d1
Create Date: 2024-06-22 00:14:58.281988

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2aa2a5ed8a3b'
down_revision: Union[str, None] = '3d73795bf6d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'author',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('author')

