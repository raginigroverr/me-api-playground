from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    education = Column(String)
    skills = Column(Text)  # store comma-separated skills
    linkedin = Column(String)
    github = Column(String)
    portfolio = Column(String)

    projects = relationship("Project", back_populates="owner")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    links = Column(String)
    owner_id = Column(Integer, ForeignKey("profiles.id"))
    owner = relationship("Profile", back_populates="projects")
