from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_PATH = os.getenv("DATABASE_PATH", "sqlite:///data.db")

engine = create_engine(DATABASE_PATH, echo=False)
Session = sessionmaker(bind=engine)

def init_db():
    from models import Base  # 延迟导入避免循环依赖
    Base.metadata.create_all(engine)
