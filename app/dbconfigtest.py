import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from fastapi import Depends

# import sqalchemy packages
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session

from typing import Annotated

DATABASE_URL = "postgresql+psycopg2://testfastdbuser:testfastdbuser1234@localhost:5432/testfastdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

"""create database connections"""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependancy = Annotated[Session,Depends(get_db)]