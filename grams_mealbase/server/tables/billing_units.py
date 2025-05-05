from .ext import TableBase
from sqlalchemy import Column, Integer, String

class BillingUnits(TableBase):
    __tablename__ = 'billing_units'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    payment_info = Column(String, nullable=False)
    plan_info = Column(String, nullable=False)