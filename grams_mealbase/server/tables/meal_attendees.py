from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey

class MealAttendees(TableBase):
    __tablename__ = "meal_attendees"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    meal_template_id = Column(Integer, ForeignKey('meal_templates.id'), nullable=False)
