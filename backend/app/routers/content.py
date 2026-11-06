from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(tags=["content"])


@router.get("/profile", response_model=schemas.ProfileOut)
def get_profile(db: Session = Depends(get_db)):
    profile = db.scalar(select(models.Profile).limit(1))
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.get("/skills", response_model=list[schemas.SkillOut])
def get_skills(db: Session = Depends(get_db)):
    return db.scalars(select(models.Skill).order_by(models.Skill.order)).all()


@router.get("/projects", response_model=list[schemas.ProjectOut])
def get_projects(
    tag: str | None = Query(default=None),
    featured: bool | None = Query(default=None),
    db: Session = Depends(get_db),
):
    query = select(models.Project).order_by(models.Project.order)
    if featured is not None:
        query = query.where(models.Project.featured == featured)

    projects = db.scalars(query).all()
    if tag:
        needle = tag.strip().lower()
        projects = [
            project
            for project in projects
            if any(needle == item.lower() for item in project.tags)
        ]
    return projects


@router.get("/projects/{slug}", response_model=schemas.ProjectOut)
def get_project(slug: str, db: Session = Depends(get_db)):
    project = db.scalar(select(models.Project).where(models.Project.slug == slug))
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/experiences", response_model=list[schemas.ExperienceOut])
def get_experiences(db: Session = Depends(get_db)):
    return db.scalars(select(models.Experience).order_by(models.Experience.order)).all()
