from .ext import TableBase
from sqlalchemy import Column, Integer, ForeignKey, Date, String

class TemporaryUnitInvitations(TableBase):
    __tablename__ = "temporary_unit_invitations"
    id = Column(Integer, primary_key=True)
    billing_unit_id = Column(Integer, ForeignKey('billing_units.id'), nullable=False)
    temporary_password_hash = Column(String, nullable=False)
    expiration_date = Column(Date, nullable=False)