import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from fastapi import APIRouter
from schemas import user_schemas
from fastapi.exceptions import HTTPException
from dbconfig import db

router = APIRouter()

@router.post("/user/create_new/")
async def create_new_user(payload: user_schemas.UserData):
    try:
        # Reference to the Firestore collection
        users_ref = db.collection("users")
        # Add a new document with the user data
        request_payload = payload.dict()
        doc_ref, _ = users_ref.add(request_payload)
        return {"message": "User created successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user/detail_user/")
def get_user_by_id(doc_id: str):
    """Fetch a user by their document ID from Firestore."""
    user_ref = db.collection("users").document(doc_id)
    user = user_ref.get()
    if user.exists:
        return user.to_dict()
    return None

@router.get("/user/user_list/")
def get_all_users():
    """Fetch all users from Firestore."""
    users_ref = db.collection("users")
    users = users_ref.stream()  # This retrieves all documents in the collection
    
    # Convert each document to a dictionary and return as a list
    user_list = [{"id": user.id, **user.to_dict()} for user in users]
    
    return user_list