from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey

class FoodAdmins(TableBase):
    __tablename__ = 'food_admins'
    id = Column(Integer, primary_key=True)
    login_id = Column(Integer, ForeignKey('logins.id'), nullable=False)