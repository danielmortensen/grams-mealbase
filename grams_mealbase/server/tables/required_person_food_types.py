from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey, Float

class RequiredPersonFoodTypes(TableBase):
    __tablename__ = "required_person_food_types"
    id = Column(Integer, primary_key=True)
    food_subtype_id = Column(Integer, ForeignKey('food_subtypes.id'), nullable=False)
    person_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    quantity = Column(Float, nullable=False)