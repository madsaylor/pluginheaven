from sqlmodel import SQLModel, Field
from datetime import datetime

class Plugin(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    image: str
    created_at: datetime
    updated_at: datetime
