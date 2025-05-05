from .ext import TableBase
from sqlalchemy import Column, Integer, String

class Logins(TableBase):
    __tablename__ = 'logins'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, unique=True, nullable=False)

   