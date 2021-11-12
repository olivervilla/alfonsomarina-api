from sqlalchemy.orm import Session

import models
import schemas

import logging

LOG = logging.getLogger(__name__)


# ---------------------------------------------
#   TEAM MATE
# ---------------------------------------------
def get_teammate(db: Session, user_id: int):
    table = schemas.Teammates.__table__
    return db.execute(table.select().where(schemas.Teammates.id == user_id)).first()


def create_teammate(db: Session, user: models.TeammateCreate):
    # TODO: hash password
    db_user = schemas.Teammates(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ---------------------------------------------
#   DEPARTMENT
# ---------------------------------------------
def get_departament(db: Session, department_id: int):
    table = schemas.Departments.__table__
    return db.execute(table.select().where(schemas.Departments.id == department_id)).first()


def get_departament_by_name(db: Session, departament_name: str):
    table = schemas.Departments.__table__
    return db.execute(table.select().where(schemas.Departments.name == departament_name)).first()


def create_department(db: Session, department: models.DepartmentCreate):
    db_department = schemas.Departments(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department
