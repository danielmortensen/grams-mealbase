from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey, Float

class AttendeeRequiredNutrients(TableBase):
    __tablename__ = "attendee_required_nutrients"
    id = Column(Integer, primary_key=True)
    attendee_id = Column(Integer, ForeignKey('meal_attendees.id'), nullable=False)
    nutrient_id = Column(Integer, ForeignKey('nutrient_types.id'), nullable=False)
    quantity = Column(Float, nullable=False)