from .ext import TableBase
from sqlalchemy import Column, Integer, Float, ForeignKey

class FoodNutrientQuantities(TableBase):
    __tablename__ = "food_nutrient_quantities"
    id = Column(Integer, primary_key=True)
    food_id = Column(Integer, ForeignKey('foods.id'), nullable=False)
    quantity = Column(Float, nullable=False)
