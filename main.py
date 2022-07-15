from turtle import position
from database.plsql import db
from models import position_model
from core import position
from core import auth
from core import user
from fastapi import FastAPI

position_model.Base.metadata.create_all(bind=db)

app = FastAPI(
    title="HrAPI",
    description="API with high performance built with FastAPI & SQLAlchemy.",
    version="1.0.0",
)
app.include_router(auth.router)
app.include_router(position.router)
app.include_router(user.router)
