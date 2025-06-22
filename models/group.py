from sqlalchemy import Column, Integer, String
from .base import Base

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_id = Column(String, unique=True, nullable=False)
    group_name = Column(String)
    admin_id = Column(String)
