from sqlalchemy.orm import Session
from . import models, schemas

def create_profile(db: Session, profile: schemas.ProfileCreate):
    db_profile = models.Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_profiles(db: Session):
    return db.query(models.Profile).all()

def create_project(db: Session, project: schemas.ProjectCreate, profile_id: int):
    db_project = models.Project(**project.dict(), owner_id=profile_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_projects(db: Session, skill: str = None):
    if skill:
        return db.query(models.Project).join(models.Profile).filter(models.Profile.skills.contains(skill)).all()
    return db.query(models.Project).all()
