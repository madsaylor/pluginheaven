"""create plugin table

Revision ID: 3d73795bf6d1
Revises: 
Create Date: 2024-06-21 23:55:55.172784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d73795bf6d1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'plugin',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        sa.Column('image', sa.String(200), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=None),
        sa.Column('updated_at', sa.DateTime, server_default=None)
    )


def downgrade() -> None:
    op.drop_table('plugin')
