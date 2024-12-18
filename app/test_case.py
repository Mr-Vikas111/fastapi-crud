# # import sys
# # import os

# # sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# import pytest
# from fastapi import Depends
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker,Session
# from app.db import Base, get_db
# from app.main import app
from fastapi.testclient import TestClient
# from models import users
# from typing import Annotated

# # Use the in-memory SQLite database
# DB_USER="testfastdbuser"
# DB_PASSWORD="testfastdb1234"
# DB_NAME="testfastdb"
# DB_SERVER="34.47.218.214"
# DB_PORT="5432"

# DATABASE_URL = SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
# # engine = create_engine(SQLALCHEMY_DATABASE_URL)
# # TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # # Override the database dependency
# # def override_db_dependency():
# #     db = TestingSessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# # app.dependency_overrides[get_db] = override_db_dependency

# # users.Base.metadata.create_all(bind=engine)  # This should create the tables
    
# # # Use FastAPI's TestClient
# # client = TestClient(app)


# # DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test_db"

# @pytest.fixture(scope="module")
# def db_session():
#     engine = create_engine(DATABASE_URL)
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#     session = SessionLocal()
#     yield session
#     session.close()


# # Example test using db_session
# def test_create_user(db_session):
#     user = users.User(mobile="8989898989",first_name="John Doe", last_name="john@example.com")
#     db_session.add(user)
#     db_session.commit()
#     db_session.refresh(user)
#     assert user.id is not None


# # @pytest.fixture(scope="module")
# # def client():
# #     """Fixture to initialize the TestClient for FastAPI"""
# #     with TestClient(app) as client:
# #         yield client
# client = TestClient(app)
# # def test_root():
# #     print("Client ->",client)
# #     response = client.get("/")
# #     assert response.status_code == 200
# #     assert response.json() == {"message": "test case running"}

# def test_create_user_api():
#     print("Running test_create_user...",client)
#     payload = {
#         "mobile": "1234567890",
#         "first_name": "John",
#         "last_name": "Doe",
#         "hashtags": [{"name": "test"}]
#     }
#     response = client.post("/user/create/", json=payload)
#     assert response.status_code == 200
#     assert response.json()["message"] == "payload created"

from unittest.mock import MagicMock
import pytest
from app.main import app
from app.db import get_db



client = TestClient(app)

@pytest.fixture
def mock_db_session():
    """Fixture for mocking the database session."""
    mock_session = MagicMock()
    yield mock_session

@pytest.fixture(autouse=True)
def override_dependency(mock_db_session):
    """Automatically override the dependency with the mock session."""
    print("override calling")
    app.dependency_overrides[get_db] = mock_db_session
    print("App.dependency ->", app.dependency_overrides)


def test_create_user(mock_db_session):
    
    print(mock_db_session.add("test"))
    print("mock testing ->",mock_db_session.add.assert_called_once_with())
    
    payload = {
        "mobile": "888888888",
        "first_name": "John",
        "last_name": "Doe",
        "hashtags": [{"name": "test"}]
    }
    
    response = client.post("/user/create/", json=payload)
    
    # Check if HTTP response is correct
    assert response.status_code == 200
    assert response.json()["message"] == "payload created"
    
    # Check if db.add() and db.commit() were called
    print(" mock_db_session.commit.assert_called_once() ->", mock_db_session.commit.assert_called_once())
    mock_db_session.add.assert_called_once()  # Ensure 'add' was called once
    mock_db_session.commit.assert_called_once()  # Ensure 'commit' was called once
    
    # Optionally, validate the object added
    # added_user = mock_db_session.add.call_args[0][0]
    # assert added_user.mobile == payload["mobile"]
    # assert added_user.first_name == payload["first_name"]
    # assert added_user.last_name == payload["last_name"]
