from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    group_id = Column(String)
    category = Column(String)
    amount = Column(Float)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
