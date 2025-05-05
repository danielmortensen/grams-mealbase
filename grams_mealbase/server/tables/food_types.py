from .ext import TableBase
from sqlalchemy import Column, Integer, String

class FoodTypes(TableBase):
    __tablename__ = "food_types"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
