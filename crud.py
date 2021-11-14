from sqlalchemy.orm import Session

from collections import Counter

import models
import schemas

import logging

LOG = logging.getLogger(__name__)


# ---------------------------------------------
#   TEAM MATE
# ---------------------------------------------
def create_teammate(db: Session, user: models.TeammateCreate):
    # TODO: hash password
    db_user = schemas.Teammates(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def read_teammate(db: Session, user_id: int):
    return db.query(schemas.Teammates).filter(schemas.Teammates.id == user_id).first()


def read_teammate_all(db: Session):
    return db.query(schemas.Teammates).all()


def update_teammate(db: Session, user: models.TeammateUpdate, user_id: int):
    db_user = read_teammate(db, user_id)
    if db_user is None:
        return None
    
    updated_data = user.dict(exclude_unset=True)
    for key, value in updated_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_teammate(db: Session, user_id: int):
    db_user = read_teammate(db, user_id)
    if db_user is None:
        return False
    db.delete(db_user)
    db.commit()
    return True


# ---------------------------------------------
#   DEPARTMENT
# ---------------------------------------------
def create_department(db: Session, department: models.DepartmentCreate):
    db_department = schemas.Departments(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def read_department(db: Session, department_id: int):
    return db.query(schemas.Departments).filter(schemas.Departments.id == department_id).first()


def read_department_all(db: Session):
    return db.query(schemas.Departments).all()


def read_department_by_name(db: Session, department_name: str):
    return db.query(schemas.Departments).filter(schemas.Departments.name == department_name).first()


def update_department(db: Session, department: models.DepartmentUpdate, department_id: int):
    db_department = read_department(db, department_id)
    if db_department is None:
        return None
    
    updated_data = department.dict(exclude_unset=True)
    for key, value in updated_data.items():
        setattr(db_department, key, value)
    db.commit()
    db.refresh(db_department)
    return db_department


def delete_department(db: Session, department_id: int):
    db_department = read_department(db, department_id)
    if db_department is None:
        return False
    db.delete(db_department)
    db.commit()
    return True


# ---------------------------------------------
#   RATING.USER
# ---------------------------------------------
def create_rating_user(db: Session, rating_user: models.RatingTeammateCreate):
    db_rating_user = schemas.RatingHistoryTeammate(**rating_user.dict(exclude_unset=True))
    db.add(db_rating_user)
    db.commit()
    db.refresh(db_rating_user)
    return db_rating_user


def read_rating_user_all(db: Session):
    return db.query(schemas.RatingHistoryTeammate).all()


def read_rating_user_by_id(db: Session, user_id: int = None):
    ratings = db.query(schemas.RatingHistoryTeammate).filter(schemas.RatingHistoryTeammate.teammate_id == user_id).all()
    if not len(ratings):
        return None
    
    # TODO: use db queries
    avg_score = sum([rating.score for rating in ratings]) / len(ratings)
    counter_badges = Counter([rating.badge.name for rating in ratings if rating.badge])

    return models.RatingTeammateAgg(avg_score=avg_score, ratings=ratings, counter_badges=counter_badges)


# ---------------------------------------------
#   RATING.DEPARTMENT
# ---------------------------------------------
def create_rating_department(db: Session, rating_department: models.RatingDepartmentCreate):
    db_rating_department = schemas.RatingHistoryDepartment(**rating_department.dict(exclude_unset=True))
    db.add(db_rating_department)
    db.commit()
    db.refresh(db_rating_department)
    return db_rating_department


def read_rating_department_all(db: Session):
    return db.query(schemas.RatingHistoryDepartment).all()


def read_rating_department_by_id(db: Session, department_id: int):
    ratings = db.query(schemas.RatingHistoryDepartment).filter(schemas.RatingHistoryDepartment.department_id == department_id).all()
    if not len(ratings):
        return None
    
    avg_score = sum([rating.score for rating in ratings]) / len(ratings)

    return models.RatingDepartmentAgg(avg_score=avg_score, ratings=ratings)

# ---------------------------------------------
#   BADGE
# ---------------------------------------------
def read_badge(db: Session, badge_id: int = None):
    return db.query(schemas.Badges).filter(schemas.Badges.id == badge_id).first()
