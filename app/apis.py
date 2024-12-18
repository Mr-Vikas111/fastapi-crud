from fastapi import Depends, APIRouter
from models import users
from schemas import user_schemas
from sqlalchemy.orm import Session
from db import get_db,engine

router = APIRouter()
users.Base.metadata.create_all(bind=engine)

@router.get("/")
async def root():
    return {"message": "test case running",}

@router.post("/user/create/")
async def create_user(payload: user_schemas.UserData, db: Session = Depends(get_db)):
    
    user = users.User(
        mobile=payload.mobile,
        first_name=payload.first_name,
        last_name=payload.last_name,
    )
    for hashtag in payload.hashtags:
        user.hashtags.append(users.HashTag(name=hashtag.name))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "payload created", "payload": payload}