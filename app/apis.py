import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from fastapi import APIRouter
from schemas.user_schemas import *
from fastapi.exceptions import HTTPException
from dbconfig import db
from typing import  Union



router = APIRouter()

# create user detail information
@router.post("/user/create/",response_model=UserRequest)
async def create_new_user(payload:  UserRequest):
    try:
        users_ref = db.collection("users")
        request_payload = payload.dict()
        _,data_ref = users_ref.add(request_payload)
        if data_ref:
            saved_data = {**request_payload, "id": data_ref.id}
            return {"message": "User created successfully!","response":saved_data}
        else:
            return {"message": "Failed","response":{}}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# retrive user detail information
@router.get("/user/detail/{user_id}",response_model=UserRequest)
def get_user_by_id(user_id: str):
    """Fetch a user by their document ID from Firestore."""
    user_ref = db.collection("users").document(user_id)
    user = user_ref.get()
    if user.exists:
        return user.to_dict()
    raise HTTPException(status_code=404, detail="User not found")

# retrive all user information
@router.get("/user/user_list/")
def get_all_users():
    """Fetch all users from Firestore."""
    users_ref = db.collection("users")
    users = users_ref.stream()
    
    user_list = [{"id": user.id, **user.to_dict()} for user in users]
    
    return user_list

# Update user information in Firestore
@router.patch("/user/update/{user_id}",response_model=UserRequest)
async def update_user(user_id: str, payload: UserRequest):
    try:
        # Reference to the user document
        doc_ref = db.collection("users").document(user_id)

        # Fetch the document to check if it exists
        doc = doc_ref.get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="User not found")
        
        payload = payload.project
       
        if payload.project_id == 1:
            update_data={
                "project_id":payload.project_id,
                "company_name":payload.company_name,
                "first_name":payload.first_name,
                "last_name":payload.last_name,
                "email": payload.email,
                "password": payload.password
                }
        if payload.project_id == 2:
            update_data = {
                'project_id':payload.project_id,
                'mobile':payload.mobile,
                'first_name': payload.first_name,
                'last_name':payload.last_name,
                'hashtags': payload.hashtags
            }
        if payload.project_id == 3:
            update_data = {
                'project_id':payload.project_id,
                'mobile':payload.mobile,
                'first_name': payload.first_name,
                'last_name':payload.last_name,
                'dob': payload.dob
            }
        # # Update the document in Firestore
        new_payload={}
        new_payload['project']=update_data
        doc_ref.update(new_payload)

        return {"message": "User updated successfully", "user_id": payload}

    except Exception as e:
        print(f"Error occurred while updating user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")



@router.delete("/user/delete/{user_id}",response_model=DeleteResponse)
async def delete_user(user_id: str):
    try:
        user_ref = db.collection("users").document(user_id)

        doc = user_ref.get()

        if not doc.exists:
            raise HTTPException(status_code=404, detail="User not found")

        user_ref.delete()
        return {"message": "User deleted successfully", "user_id": user_id}

    except Exception as e:
        # If any error occurs, raise an internal server error
        raise HTTPException(status_code=500, detail=str(e))