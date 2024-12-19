from pydantic import BaseModel, Field, ValidationError, validator,EmailStr
from typing import List, Optional
from datetime import date
from datetime import date,datetime

class TeamMember(BaseModel):
    name: str
    role: str

def convert_to_datetime(dob: date) -> datetime:
    return datetime(dob.year, dob.month, dob.day)

class ProjectDetails(BaseModel):
    start_date: date
    end_date: date
    team_members: List[TeamMember]
    
    @validator('start_date')
    def validate_and_convert_start_date(cls, v):
        # Convert datetime.date to datetime.datetime for Firestore compatibility
        return convert_to_datetime(v)
      
    @validator('end_date')
    def validate_and_convert_end_date(cls, v):
        # Convert datetime.date to datetime.datetime for Firestore compatibility
        return convert_to_datetime(v)

class Project(BaseModel):
    project_id: int
    name: str
    details: ProjectDetails

class Contact(BaseModel):
    email: EmailStr
    phone: str

class Employee(BaseModel):
    name: str
    contact: Contact
    projects: List[Project]
