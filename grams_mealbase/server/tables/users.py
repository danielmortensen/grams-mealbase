from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey

class Users(TableBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login_id = Column(Integer, ForeignKey('logins.id'), nullable=False)
    person_id = Column(Integer, ForeignKey('people.id'), nullable=False)