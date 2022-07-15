from turtle import pos
from sqlalchemy.orm import Session
from models import position_model
from schema import schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    return db.query(position_model.Position).with_entities(position_model.Position.id, position_model.Position.name).all()

def create(request: schemas.NewPosition, db: Session):
    position = position.Position(name=request.name)
    db.add(position)
    db.commit()
    db.refresh(position)
    return {"id":position.id,"name": position.name}

def show(id: int, db: Session):
    position = db.query(position_model.Position).filter(position_model.Position.id == id).with_entities(position_model.Position.id, position_model.Position.name).first()
    if not position:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Position with id {id} not found"
        )
    return position