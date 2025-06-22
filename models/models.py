from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from . import Base

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    telegram_id = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    amount = Column(Float)
    category = Column(String)
    note = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserWallet(Base):
    __tablename__ = 'wallets'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    address = Column(String, unique=True)
    phone_number = Column(String)
    remark = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
