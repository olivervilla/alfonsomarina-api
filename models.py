from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

# TODO: all <field>_id create enum, if possible

# ---------------------------------------------
#   DEPARTMET
# ---------------------------------------------
class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    name: str
    score: Optional[float] = None

    class Config:
        orm_mode = True


class Badge(BaseModel):
    id: int
    name: str
    value: int

    class Config:
        orm_mode = True


class CommentTeammate(BaseModel):
    id: int
    datetime: datetime
    teammate_id: int
    comment: str

    # teammate = relationship("Teammates", back_populates="teammates", uselist=False)
    # teammate: TeammateBase

    class Config:
        orm_mode = True


class TeammateBase(BaseModel):
    id: int
    firstname: str
    lastname: str
    age: Optional[int] = None
    # department = Column(Integer, ForeignKey("departments.id"))
    department_id: int
    score: Optional[float] = None

    # department: Department
    # badges: List[Badge]
    # comments: List[CommentTeammate]


class TeammateCreate(TeammateBase):
    password: str
    # score: Optional[float] = 0.0


class Teammate(TeammateBase):
    class Config:
        orm_mode = True