from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base

class Wallet(Base):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True)
    address = Column(String, unique=True)
    remark = Column(String)
    owner_id = Column(String)
    label = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
