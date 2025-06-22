from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from utils.config import DATABASE_PATH

engine = create_engine(f'sqlite:///{DATABASE_PATH}', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    from .models import Group, Record, UserWallet
    Base.metadata.create_all(engine)
