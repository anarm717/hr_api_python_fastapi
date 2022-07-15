#!/usr/bin/python3


from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.plsql import get_session
from models import user_model
from schema import schemas
from schema.hash import Hash
from schema.token import create_access_token

router = APIRouter(prefix="/login", tags=["Authentication"],)


@router.post("/")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_session),
):
    """
    Login user

    Args:
        request (OAuth2PasswordRequestForm, optional): OAuth2PasswordRequestForm.
        db (Session, optional): Session. Defaults to Depends(configuration.get_db).

    Raises:
        HTTPException: 401 Unauthorized
        HTTPException: 404 Not Found

    Returns:
        Hash: Hash
    """
    user: schemas.User = db.query(user_model.User).filter(
        user_model.User.email == request.username
    ).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )

    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password"
        )

    access_token = create_access_token(data={"sub": user.email})

    # generate JWT token and return
    return {"access_token": access_token, "token_type": "bearer"}
