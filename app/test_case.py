import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import pytest
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from app.dbconfigtest import Base, get_db
from app.main import app
from fastapi.testclient import TestClient
from models import users
from typing import Annotated


DB_USER="testfastdbuser"
DB_PASSWORD="testfastdb1234"
DB_NAME="testfastdb"
DB_SERVER="34.47.218.214"
DB_PORT="5432"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print("test")
def init_db():
    # Create the tables for the test database
    Base.metadata.create_all(bind=engine)

def drop_db():
    # Drop all tables after the tests
    Base.metadata.drop_all(bind=engine)


client = TestClient(app)

# Setup the database for testing
@pytest.fixture(scope="function")
def db():
    init_db()
    yield TestingSessionLocal()
    drop_db()

@pytest.fixture(scope="function")
def client_with_db(db):
    # Override the dependency to use the test DB session
    app.dependency_overrides[get_db] = lambda: db
    yield client
    del app.dependency_overrides[get_db]


# Example test case
def test_create_user(client_with_db):
    print("app dependancy ->",app.dependency_overrides)
    print("Test Database URL:", engine.url)

    payload = {
        "mobile": "6758948758",
        "first_name": "John",
        "last_name": "Doe",
        "hashtags": [{"name": "test"}]
    }
    response = client_with_db.post("/user/create/", json=payload)
    print("response ->",response)
    assert response.status_code == 200
    # assert response.json() == 