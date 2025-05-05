from .ext import TableBase
from sqlalchemy import Column, Integer, Date, ForeignKey

class MealPlans(TableBase):
    __tablename__ = "meal_plans"
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    meal_template_id = Column(Integer, ForeignKey('meal_templates.id'), nullable=False)
    