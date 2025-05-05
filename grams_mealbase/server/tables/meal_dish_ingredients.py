from .ext import TableBase
from sqlalchemy import Column, Integer, Float, ForeignKey

class MealDishIngredients(TableBase):
    __tablename__ = "meal_dish_ingredients"
    id = Column(Integer, primary_key=True)
    meal_dish_id = Column(Integer, ForeignKey('meal_dishes.id'), nullable=False)
    preparation_type_id = Column(Integer, ForeignKey('preparation_types.id'), nullable=False)
    food_id = Column(Integer, ForeignKey('foods.id'), nullable=False)
    ratio = Column(Float, nullable=False)