"""load data

Revision ID: 3c0fb18dc932
Revises: 68de4ef4947c
Create Date: 2024-06-24 12:56:46.565603

"""

from typing import Sequence, Union
import json
from datetime import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from os import path
from models import Plugin

# revision identifiers, used by Alembic.
revision: str = '3c0fb18dc932'
down_revision: Union[str, None] = '68de4ef4947c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def load_data(session: Session) -> None:
    # get ../data/plugin_1699142582.json file path using os module
    current_dir = path.dirname(__file__)
    data_file = path.join(path.dirname(current_dir), 'data', 'plugin_1699142582.json')

    print(f"Importing data from {data_file}")

    with (open(data_file, 'r') as f):
        data = f.read()
        data_dict = json.loads(data)
        i = 0
        for plugin_id, plugin_data in data_dict['ret'].items():
            if (
                    plugin_id != '__bubble_tz_string_in_body' and
                    'price' in plugin_data and
                    plugin_data['price'] is not None
            ):
                plugin = Plugin(
                    uuid=plugin_id,
                    title=plugin_data['display'],
                    description=plugin_data['description'],
                    price=plugin_data['price'],
                    one_time_price=plugin_data['one_time_price'],
                    image=plugin_data['icon'],
                    created_at=datetime.fromtimestamp(int(plugin_data['published_date'])/1000),
                    count=plugin_data['count'],
                )
                session.add(plugin)
                session.commit()
                i += 1
                if i % 100 == 0:
                    print(f"Inserted {i} plugins")


def upgrade() -> None:
    session = Session(op.get_bind())
    load_data(session)


def downgrade() -> None:
    session = Session(op.get_bind())
    session.query(Plugin).delete()
