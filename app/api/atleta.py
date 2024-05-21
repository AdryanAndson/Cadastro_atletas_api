from sqlite3 import IntegrityError
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi_pagination import Page, add_pagination, paginate

from app.schemas.atleta import AtletaCreate, AtletaResponse
from app.crud.atleta import get_atletas, create_atleta
from app.db.session import get_db

router = APIRouter()

@router.get("/atletas", response_model=Page[AtletaResponse])
def read_atletas(nome: str = None, cpf: str = None, db: Session = Depends(get_db)):
    atletas = get_atletas(db, nome, cpf)
    return paginate(atletas)

@router.post("/atletas", response_model=AtletaResponse)
def create_new_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    try:
        new_atleta = create_atleta(db, atleta)
        return new_atleta
    except IntegrityError as e:
        raise HTTPException(status_code=303, detail=str(e))
