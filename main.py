from typing import Union
from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def initial():
    database = 'postgresql://postgres:mysecretpassword@localhost/postgres'
    engine = create_engine(database)
    SQLModel.metadata.create_all(engine)

