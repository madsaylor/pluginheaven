from typing import Union
from fastapi import FastAPI
from sqlmodel import SQLModel, Session, create_engine, funcfilter
import json

from models import Plugin

db_url = 'postgresql://postgres:mysecretpassword@localhost/postgres'
engine = create_engine(db_url, echo=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_data()
    yield


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


app = FastAPI(lifespan=lifespan)
