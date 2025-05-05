from .ext import TableBase
from sqlalchemy import Column, Integer, String, ForeignKey

class FoodSubtypes(TableBase):
    __tablename__ = "food_subtypes"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    food_type_id = Column(Integer, ForeignKey('food_types.id'), nullable=False)
    