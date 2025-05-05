from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey

class PersonDietaryRestrictions(TableBase):
    __tablename__ = "person_dietary_restrictions"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    dietary_restriction_type_id = Column(Integer, ForeignKey('dietary_restriction_types.id'), nullable=False)