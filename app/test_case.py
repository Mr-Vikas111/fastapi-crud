import sys
import os

# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app  # Your FastAPI app


def get_db():
    return []


@pytest.fixture
def mock_db():
    """Fixture to provide a mocked database."""
    return [
       {
        "project_id": 1,
        "company_name": "string",
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "CBx?sr&k%BA0YsQYHiGG8q"
        },
       {
        "project_id": 1,
        "company_name": "string",
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "CBx?sr&k%BA0YsQYHiGG8q"
        }
    ]


@pytest.fixture
def override_get_db(mock_db):
    app.dependency_overrides[get_db] = lambda: mock_db
    yield
    app.dependency_overrides.clear()
    

# Test client setup
@pytest.fixture
def client():
    """Fixture to set up the TestClient."""
    return TestClient(app)

# Test case to check the response of the /users/ endpoint
def test_get_all_users(client, mock_db):
    """Test the /users/ endpoint that returns all users."""
    response = client.get("/user/user_list/")
    # print("response.dict()",response.dict())
    # Assert that the status code is 200 OK
    assert response.status_code == 200


""" ### Create User instance api testing """
def test_project_one_create_user_success(client,mock_db, override_get_db):
    """Test successful user creation."""
    payload = {
        "project_id": 1,
        "company_name": "string",
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "CBx?sr&k%BA0YsQYHiGG8q"
        }
        
    response = client.post("/user/create/", json=payload)
    assert response.status_code == 200
    data = response.json()
    print("data",data)
    assert data["response"]['company_name'] == "string"


def test_project_two_create_user_success(client,mock_db, override_get_db):
    """Test successful user creation."""
    payload = {
        "project_id": 2,
        "mobile": "9098987678",
        "first_name": "kisan",
        "last_name": "singh",
        "hashtags":["test_hash","testhash_2"]
        }
        
    response = client.post("/user/create/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["response"]['mobile'] == "9098987678"



def test_project_three_create_user_success(client,mock_db, override_get_db):
    """Test successful user creation."""
    payload = {
        "project_id": 3,
        "mobile": "9098987678",
        "first_name": "kisan",
        "last_name": "singh",
        "dob":"2023-05-12"
        }
        
    response = client.post("/user/create/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["response"]['mobile'] == "9098987678"
    assert data["response"]['dob'] == "2023-05-12T00:00:00"
    

""" ### Update User instance api testing """
def test_project_one_update_user_success(client,mock_db, override_get_db):
    """Test successful user creation."""
    payload = {
        "project_id": 1,
        "company_name": "test_company",
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "email": "user@example.com",
        "password": "CBx?sr&k%BA0YsQYHiGG8q"
        }
    user_id = "TgCpp08IjAyLdOi8FCm0"
    response = client.patch(f"/user/update/{user_id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    print("data",data)
    assert data['user_id']['company_name'] == "test_company"
    
    
def test_project_two_update_user_success(client,mock_db, override_get_db):
    """Test successful user creation."""
    payload = {
        "project_id": 2,
        "mobile": "9098987600",
        "first_name": "kisan soni",
        "last_name": "singh",
        "hashtags":["test_hash_3","testhash_4"]
        }
    user_id = "RpaqoVYJdcTvc1OIZW6f"
    response = client.patch(f"/user/update/{user_id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    print("data",data)
    assert data['user_id']['mobile'] == "9098987600"

def test_project_three_update_user_success(client,mock_db, override_get_db):
    """Test successful user creation."""
    payload =  {
        "project_id": 3,
        "mobile": "9098987678",
        "first_name": "op singh",
        "last_name": "yadav",
        "dob":"2023-05-24"
        }
    user_id = "1i0vnfFdWirVCBaLc1VW"
    response = client.patch(f"/user/update/{user_id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    print("data",data)
    assert data['user_id']['mobile'] == "9098987678"