from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey, String

class Foods(TableBase):
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    food_subtype_id = Column(Integer, ForeignKey('food_subtypes.id'), nullable=False)