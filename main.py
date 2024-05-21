from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Atletas"}

from fastapi_pagination import add_pagination
add_pagination(app)
