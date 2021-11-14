from typing import List, Optional
from datetime import date, datetime
from collections import Counter

from pydantic import BaseModel

# TODO: all <field>_id create enum, if possible

# ---------------------------------------------
#   DEPARTMET
# ---------------------------------------------
class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    score: Optional[float]
    name: Optional[str]

class Department(DepartmentBase):
    id: int
    score: Optional[float] = None

    class Config:
        orm_mode = True


# ---------------------------------------------
#   BADGE
# ---------------------------------------------
class Badge(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# ---------------------------------------------
#   RATING.TEAMMATE
# ---------------------------------------------
class RatingTeammateBase(BaseModel):
    teammate_id: int
    score: float
    comment: Optional[str]

class RatingTeammateCreate(RatingTeammateBase):
    badge_id: Optional[int]

class RatingTeammate(RatingTeammateBase):
    # id: int
    datetime: datetime
    badge: Optional[Badge]
    
    class Config:
        orm_mode = True

class RatingTeammateAgg(BaseModel):
    avg_score: float
    counter_badges: Counter
    ratings: List[RatingTeammate]


# ---------------------------------------------
#   RATING.DEPARTMENT
# ---------------------------------------------
class RatingDepartmentBase(BaseModel):
    department_id: int
    score: float
    comment: Optional[str]

class RatingDepartmentCreate(RatingDepartmentBase):
    pass

class RatingDepartment(RatingDepartmentBase):
    # id: int
    datetime: datetime

    class Config:
        orm_mode = True

class RatingDepartmentAgg(BaseModel):
    avg_score: float
    ratings: List[RatingDepartment]
    

# ---------------------------------------------
#   TEAMMATE
# ---------------------------------------------
class TeammateBase(BaseModel):
    id: int
    firstname: str
    lastname: str
    age: Optional[int] = None
    department_id: int

class TeammateCreate(TeammateBase):
    password: str
    # score: Optional[float] = 0.0

class TeammateUpdate(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    age: Optional[int]
    department_id: Optional[int]

class Teammate(TeammateBase):
    # department: Department
    # badges: List[Badge]
    ratings: List[RatingTeammate]

    class Config:
        orm_mode = True
