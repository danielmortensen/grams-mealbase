from .ext import TableBase
from sqlalchemy import Column, Integer, String

class DietaryRestrictionTypes(TableBase):
    __tablename__ = "dietary_restriction_types"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)