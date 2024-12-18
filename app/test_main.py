# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.main import app
# from app.db import Base, get_db
# import os

# # Test database URL
# SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"

# # Create a new database engine for testing
# engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Dependency override to use the test database
# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Apply the override in FastAPI
# app.dependency_overrides[get_db] = override_get_db

# @pytest.fixture(scope="module", autouse=True)
# def create_test_db():
#     print("Dependency Overrides:", app.dependency_overrides)

#     Base.metadata.create_all(bind=engine)
#     yield
#     Base.metadata.drop_all(bind=engine)

# @pytest.fixture(scope="module")
# def client():
#     """Fixture to initialize the TestClient for FastAPI"""
#     with TestClient(app) as client:
#         yield client

# # Example test case
# def test_create_user(client):
#     print("app dependancy ->",app.dependency_overrides)
#     print("Test Database URL:", engine.url)

#     payload = {
#         "mobile": "9876789876787678",
#         "first_name": "John",
#         "last_name": "Doe",
#         "hashtags": [{"name": "test"}]
#     }
#     response = client.post("/user/create/", json=payload)
#     print("response ->",response)
#     assert response.status_code == 200
#     # assert response.json() == 

# # def test_get_user(client):
# #     # Assuming the user with ID 1 exists
# #     response = client.get("/users/1/")
# #     assert response.status_code == 200
# #     assert response.json() == {"name": "John Doe", "email": "john@example.com", "id": 1}
