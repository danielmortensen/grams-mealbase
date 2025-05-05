from .ext import TableBase
from sqlalchemy import Column, Integer, Float, ForeignKey

class RequiredPersonNutrients(TableBase):
    __tablename__ = "required_person_nutrients"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    nutrient_id = Column(Integer, ForeignKey('nutrient_types.id'), nullable=False)
    quantity = Column(Float, nullable=False)