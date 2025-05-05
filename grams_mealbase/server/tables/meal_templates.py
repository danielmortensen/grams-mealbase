from .ext import TableBase
from sqlalchemy import Column, Integer, String, ForeignKey

class MealTemplates(TableBase):
    __tablename__ = "meal_templates"
    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, ForeignKey('meal_types.id'), nullable=False)
    preparer_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    name = Column(String, nullable=False)
