from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Me API Playground")

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/profiles/", response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    return crud.create_profile(db, profile)

@app.get("/profiles/", response_model=list[schemas.Profile])
def get_profiles(db: Session = Depends(get_db)):
    return crud.get_profiles(db)

@app.post("/profiles/{profile_id}/projects/", response_model=schemas.Project)
def create_project(profile_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, project, profile_id)

@app.get("/projects/", response_model=list[schemas.Project])
def get_projects(skill: str = None, db: Session = Depends(get_db)):
    return crud.get_projects(db, skill)
