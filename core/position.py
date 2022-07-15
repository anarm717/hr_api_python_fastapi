from turtle import position
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from api import position
from database.plsql import get_session
from typing import List
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["Positions"], prefix="/positions")

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Position])
def get_positions(db: Session = Depends(get_session),current_user: schemas.User = Depends(get_current_user)):
    return position.get_all(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Position)
def get_position_by_id(id: int, db: Session = Depends(get_session),current_user: schemas.User = Depends(get_current_user)):
    return position.show(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Position)
def create_position(request: schemas.NewPosition, db: Session = Depends(get_session),current_user: schemas.User = Depends(get_current_user)):
    return position.create(request, db)