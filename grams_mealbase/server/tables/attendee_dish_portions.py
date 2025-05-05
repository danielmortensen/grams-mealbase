from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey, Float

class AttendeeDishPortions(TableBase):
    __tablename__ = "attendee_dish_portions"
    id = Column(Integer, primary_key=True)
    selected_dish_id = Column(Integer, ForeignKey('selected_dishes.id'), nullable=False)
    quantity = Column(Float, nullable=False)