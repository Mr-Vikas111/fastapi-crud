from pydantic import BaseModel


class HashTag(BaseModel):
    name:str

class UserData(BaseModel):
    mobile:str
    first_name:str
    last_name:str
    hashtags:list[HashTag]