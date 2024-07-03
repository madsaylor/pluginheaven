from sqlmodel import SQLModel, Field, Column, Computed
from datetime import datetime
from sqlalchemy.dialects.postgresql import TEXT, TSVECTOR
import sqlalchemy as sa
from typing import ClassVar


def to_tsvector(*columns):
    s = " || ' ' || ".join(columns)
    return sa.func.to_tsvector(sa.text("'english'"), sa.text(s))


class Plugin(SQLModel, table=True):
    uuid: str | None = Field(default=None, primary_key=True)
    title: str = Field(sa_column=Column(TEXT))
    description: str = Field(sa_column=Column(TEXT))
    image: str = Field(max_length=2048)
    created_at: datetime
    price: int | None
    one_time_price: int | None
    image: str
    count: int = Field(index=True)

    __table_args__ = (
        sa.Index(
            "ix_index_name",
            to_tsvector('title', 'description'),
            postgresql_using="gin",
        ),
    )

    # tags: ARRAY['Tag'] = Field(default=[])


# class Tag(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     name: str

