from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey 

class Royals(TableBase):
    __tablename__ = 'royals'
    id = Column(Integer, primary_key=True)
    login_id = Column(Integer, ForeignKey('logins.id'), nullable=False)