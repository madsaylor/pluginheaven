from typing import Annotated

from fastapi import FastAPI, Request, Form
from sqlmodel import Session, create_engine, select
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import Plugin

db_url = 'postgresql://postgres:mysecretpassword@localhost/postgres'
engine = create_engine(db_url, echo=True)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


@app.get("/plugins")
def get_plugins_json():
    with Session(engine) as session:
        plugins = session.query(Plugin).limit(50).all()
        return plugins


@app.get("/", response_class=HTMLResponse)
def get_plugins(request: Request):
    with Session(engine) as session:
        plugins = session.exec(select(Plugin).limit(50))
        return templates.TemplateResponse(
            request=request, name="index.html", context={"plugins": plugins}
        )


@app.post("/search", response_class=HTMLResponse)
def search_plugin(request: Request, search: str = Form(default=""), sort: str = Form(default="")):
    with Session(engine) as session:
        if len(search) == 0 and len(sort) == 0:
            plugins = session.exec(select(Plugin).limit(50))
        else:
            # search within description and title
            criteria = None
            if len(sort) > 0:
                criteria = Plugin.count.desc() if sort.split(':')[1] == 'desc' else Plugin.count.asc()

            plugins = session.exec(
                select(Plugin)
                .filter(
                    Plugin.title.ilike(f"%{search}%") | Plugin.description.ilike(f"%{search}%")
                )
                .limit(50)
                .order_by(criteria)
            )

        return templates.TemplateResponse(
            request=request, name="plugins.html", context={"plugins": plugins}
        )

