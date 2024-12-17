from fastapi import Depends

# import sqalchemy packages
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session

from typing import Annotated

import config


# Database connection settings
DB_USER=config.DB_USER
DB_PASSWORD=config.DB_PASSWORD
DB_NAME=config.DB_NAME
DB_SERVER=config.DB_SERVER
DB_PORT=config.DB_PORT

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

"""create database connections"""

def get_db():
    db = SessionLocal()
    print("db ->",db)

    try:
        yield db
    finally:
        db.close()

db_dependancy = Annotated[Session,Depends(get_db)]