from pydantic import BaseModel
from typing import List, Optional

class ProjectBase(BaseModel):
    title: str
    description: str
    links: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        from_attributes = True  # instead of orm_mode

class ProfileBase(BaseModel):
    name: str
    email: str
    education: str
    skills: str
    linkedin: Optional[str]
    github: Optional[str]
    portfolio: Optional[str]

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    projects: List[Project] = []

    class Config:
        from_attributes = True  # instead of orm_mode

    
