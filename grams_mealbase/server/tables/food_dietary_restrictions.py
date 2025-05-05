from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey

class FoodDietaryRestrictions(TableBase):
    __tablename__ = "food_dietary_restrictions"
    id = Column(Integer, primary_key=True)
    food_id = Column(Integer, ForeignKey('foods.id'), nullable=False)
    dietary_restriction_type_id = Column(Integer, ForeignKey('dietary_restriction_types.id'), nullable=False)
