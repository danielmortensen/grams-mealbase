from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey, Float

class SelectedDishes(TableBase):
    __tablename__ = "selected_dishes"
    id = Column(Integer, primary_key=True)
    meal_plan_id = Column(Integer, ForeignKey('meal_plans.id'), nullable=False)
    meal_dish_id = Column(Integer, ForeignKey('meal_dishes.id'), nullable=False)
    quantity = Column(Float, nullable=False)