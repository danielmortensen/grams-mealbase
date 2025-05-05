from .ext import TableBase
from sqlalchemy import Column, Integer, String, Date

class TemporaryLogins(TableBase):
    __tablename__ = "temporary_logins"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, unique=True, nullable=False)
    expiration = Column(Date,  nullable=False)
    name = Column(String, nullable=False)


