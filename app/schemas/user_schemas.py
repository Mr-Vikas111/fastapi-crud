from pydantic import BaseModel, Field, ValidationError, validator,EmailStr
from typing import List, Optional, Union, Literal
import re
from enum import Enum
from datetime import date,datetime
    
# schema for create user
class HashTag(BaseModel):
    name:str

##### CONDITIONAL REQUEST BODY DESIGN

class ProjectOne(BaseModel):
    project_id: Literal[1]
    company_name:str
    first_name:str
    last_name:str
    email:EmailStr
    password:str = Field(
        ...,
        pattern=r"^[A-Za-z\d@$!%*?&]{8,}$",
        description="Password must be at least 8 characters long and may include letters, numbers, and special characters @$!%*?&."
    )

# class HashTag:
#     def __init__(self, name: str):
#         self.name = name


class ProjectTwo(BaseModel):
    project_id: Literal[2]
    mobile:str = Field(..., pattern=r"^\+?[1-9]\d{1,14}$")
    first_name:str
    last_name:str
    hashtags:List[str]
    
    @validator("mobile")
    def validate_mobile(cls, value):
        if not re.match(r"^\+?[1-9]\d{9,14}$", value):  # Example: 10-15 digits
            raise ValueError("Mobile number must be in valid format.")
        return value
    
    class Config:
        arbitrary_types_allowed = True

def convert_to_datetime(dob: date) -> datetime:
    return datetime(dob.year, dob.month, dob.day)

class ProjectThree(BaseModel):
    project_id: Literal[3]
    mobile:str
    first_name:str
    last_name:str
    dob: date 
    
    @validator("mobile")
    def validate_mobile(cls, value):
        if not re.match(r"^\+?[1-9]\d{9,14}$", value):  # Example: 10-15 digits
            raise ValueError("Mobile number must be in valid format.")
        return value
    
    
    @validator('dob')
    def validate_and_convert_dob(cls, v):
        # Convert datetime.date to datetime.datetime for Firestore compatibility
        return convert_to_datetime(v)

class UserRequest(BaseModel):
    project: Union[ProjectOne, ProjectTwo, ProjectThree]