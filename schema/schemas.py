from pydantic import BaseModel
from typing import Optional

class Position(BaseModel):
    id: int
    name: str

class NewPosition(BaseModel):
    name: str

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True