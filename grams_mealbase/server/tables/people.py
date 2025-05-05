from .ext import TableBase
from sqlalchemy import Column, Integer, String, ForeignKey

class People(TableBase):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    billing_unit_id = Column(Integer, ForeignKey('billing_units.id'), nullable=False)
