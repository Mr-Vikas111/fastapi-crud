import sys
import os

# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app  # Your FastAPI app


# Mocking Firestore
@pytest.fixture
def mock_firestore():
    """Fixture to mock Firestore interactions."""
    # Create a mock object for Firestore collection
    mock_collection = MagicMock()
    
    # Create mock documents
    mock_doc1 = MagicMock()
    mock_doc1.id = "doc_id_1"
    mock_doc1.to_dict.return_value = {
        "first_nam": "John Doe",
        "last_name": "Bin",
        "mobile":"786590889",
        "hashtags":[
            {"name":"health"}
        ]
    }
    
    mock_doc2 = MagicMock()
    mock_doc2.id = "doc_id_2"
    mock_doc2.to_dict.return_value = {
        "first_nam": "John Doe",
        "last_name": "Bin",
        "mobile":"786590889",
        "hashtags":[
            {"name":"health"}
        ]
    }
    
    # Simulate the collection stream
    mock_collection.stream.return_value = [mock_doc1, mock_doc2]
    
    # Return the mock collection object
    return mock_collection

# Mocking the database call to Firestore
@pytest.fixture
def mock_db(monkeypatch, mock_firestore):
    """Patch the Firestore database."""
    monkeypatch.setattr("dbconfig.db", mock_firestore)
    print("monkeypatch.setattr("", mock_firestore)")

# Test client setup
@pytest.fixture
def client():
    """Fixture to set up the TestClient."""
    return TestClient(app)

# Test case to check the response of the /users/ endpoint
def test_get_all_users(client, mock_db):
    """Test the /users/ endpoint that returns all users."""
    response = client.get("/user/user_list/")

    # Assert that the status code is 200 OK
    assert response.status_code == 200