from xmlrpc.client import Boolean
from database.plsql import Base
import datetime
from sqlalchemy import Column, Integer, String,BOOLEAN, DateTime

class Position(Base):
    __tablename__ = "positions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,nullable = False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime,nullable = True)
    status = Column(BOOLEAN, server_default='t')