from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from functools import lru_cache
from .. import config

engine = create_engine(config.sqlalchemy_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close() 