import pytest
from app.main import app  # Import your FastAPI app
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from sqlalchemy.orm import Session

@pytest.fixture
def client():
    client = TestClient(app)
    return client

@pytest.fixture
def mock_db():
    db = MagicMock(spec=Session)
    return db

app.dependency_overrides = { "db_dependancy": lambda: mock_db() }

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200

# def test_create_user(client,mock_db):
#     response = client.post("/user/create/")
#     data = {
#     "mobile": "9089878786",
#     "first_name": "harry",
#     "last_name": "singh",
#     "hashtags": [
#         {
#         "name": "sports"
#         }
#     ]
#     }
#     # Send POST request to the endpoint with the data
#     response = client.post("/user/create/", json=data)
    
#     # Assert the response status code
#     assert response.status_code == 200
#     # Assert the response body matches the sent data
#     # assert response.json() == data

