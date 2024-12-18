from pydantic import BaseModel
from typing import List, Optional

# schema for create user
class HashTag(BaseModel):
    name:str

class UserData(BaseModel):
    mobile:str
    first_name:str
    last_name:str
    hashtags:List[HashTag]


# schema for get user detail
class HashTagDetail(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class UserDetail(BaseModel):
    id: int
    first_name: str
    last_name: str
    mobile: str
    hashtags: List[HashTagDetail]

    class Config:
        orm_mode = True