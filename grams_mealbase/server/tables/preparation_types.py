from .ext import TableBase
from sqlalchemy import Column, Integer, String

class PreparationTypes(TableBase):
    __tablename__ = "preparation_types"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)