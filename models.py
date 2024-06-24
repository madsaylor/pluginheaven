from sqlmodel import SQLModel, Field, String
from datetime import datetime
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy import Column


class Plugin(SQLModel, table=True):
    uuid: str | None = Field(default=None, primary_key=True)
    title: str = Field(sa_column=Column(TEXT))
    description: str = Field(sa_column=Column(TEXT))
    image: str = Field(max_length=2048)
    created_at: datetime
    price: int | None
    one_time_price: int | None
    image: str
    count: int
    # tags: ARRAY['Tag'] = Field(default=[])


# class Tag(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     name: str

