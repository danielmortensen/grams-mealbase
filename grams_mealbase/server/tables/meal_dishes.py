from .ext import TableBase
from sqlalchemy import Column, Integer, String, Boolean

class MealDishes(TableBase):
    __tablename__ = "meal_dishes"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    instructions = Column(String, nullable=False)
    to_remove = Column(Boolean, nullable=False)