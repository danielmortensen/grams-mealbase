from .ext import TableBase
from sqlalchemy import Column, Integer, String 

class NutrientTypes(TableBase):
    __tablename__ = "nutrient_types"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
