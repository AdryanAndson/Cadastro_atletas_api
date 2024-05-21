from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.atleta import Atleta
from app.schemas.atleta import AtletaCreate

def get_atletas(db: Session, nome: str = None, cpf: str = None):
    query = db.query(Atleta)
    if nome:
        query = query.filter(Atleta.nome == nome)
    if cpf:
        query = query.filter(Atleta.cpf == cpf)
    return query.all()

def create_atleta(db: Session, atleta: AtletaCreate):
    new_atleta = Atleta(**atleta.dict())
    try:
        db.add(new_atleta)
        db.commit()
        db.refresh(new_atleta)
        return new_atleta
    except IntegrityError:
        db.rollback()
        raise IntegrityError(f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
