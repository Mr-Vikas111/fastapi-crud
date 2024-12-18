import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "db_cred.json"
db = firestore.Client()

def get_all_users():
    """Fetch all users from Firestore along with their document IDs."""
    users_ref = db.collection("users")
    users = users_ref.stream()  # Retrieves all documents in the collection
    
    # Convert each document to a dictionary and include its document ID
    user_list = [{"id": user.id, **user.to_dict()} for user in users]
    
    return user_list

