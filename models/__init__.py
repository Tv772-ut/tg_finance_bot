from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
import os

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    name = Column(String(100))
    records = relationship("Record", back_populates="user")

class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    amount = Column(Float)
    category = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="records")

# 获取数据库路径
DB_PATH = os.getenv("DB_PATH", "sqlite:///finance.db")

# 创建数据库引擎
engine = create_engine(DB_PATH, echo=False)
Base.metadata.create_all(engine)

# 创建会话工厂
Session = sessionmaker(bind=engine)
