import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Add the root project directory to sys.path
from fastapi import FastAPI
from db import engine,db_dependancy
from models import users
from schemas import user_schemas

app = FastAPI()

# db migrations
users.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "test case running",}



# @app.post("/user/create/")
# async def create_user(payload: user_schemas.UserData, db: db_dependancy):
#     user = users.User(
#         mobile=payload.mobile,
#         first_name=payload.first_name,
#         last_name=payload.last_name,
#     )
#     for hashtag in payload.hashtags:
#         user.hashtags.append(users.HashTag(name=hashtag.name))
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return {"message": "payload created", "payload": payload}
