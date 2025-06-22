# models/schemas.py

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

Base = declarative_base()

class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    amount = Column(Float)
    category = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

DATABASE_URL = "sqlite:///finance.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
