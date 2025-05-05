from .ext import TableBase
from sqlalchemy import Column, Integer, String

class MealTypes(TableBase):
    __tablename__ = 'meal_types'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)