from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

# TODO: default score = 0.0
# TODO: unique department

# TODO: score has to be calculated, relationship?
class Teammates(Base):
    __tablename__ = "teammates"

    id = Column(Integer, primary_key=True, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer, nullable=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    password = Column(String)

    department = relationship("Departments", back_populates="teammate", uselist=False)
    ratings = relationship("RatingHistoryTeammate", back_populates="teammate")


# TODO: score has to be calculated, relationship?
class Departments(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)

    teammate = relationship("Teammates", back_populates="department", uselist=False)
    ratings = relationship("RatingHistoryDepartment", back_populates="department")


class RatingHistoryTeammate(Base):
    __tablename__ = "rating_hist_teammate"
    
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    datetime = Column(DateTime, server_default=func.now())
    teammate_id = Column(Integer, ForeignKey("teammates.id"))
    score = Column(Float)
    comment = Column(String, nullable=True)
    badge_id = Column(Integer, ForeignKey("badges.id"), nullable=True)
    
    badge = relationship("Badges", back_populates="rating", uselist=False)
    teammate = relationship("Teammates", back_populates="ratings", uselist=False)


class RatingHistoryDepartment(Base):
    __tablename__ = "rating_hist_department"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    datetime = Column(DateTime, server_default=func.now())
    department_id = Column(Integer, ForeignKey("departments.id"))
    score = Column(Float)
    comment = Column(String, nullable=True)

    department = relationship("Departments", back_populates="ratings", uselist=False)


class Badges(Base):
    __tablename__ = "badges"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    # value = Column(Integer)

    rating = relationship("RatingHistoryTeammate", back_populates="badge", uselist=False)


# class BadgesHistory(Base):
#     __tablename__ = "badges_hist"

#     id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     datetime = Column(DateTime, server_default=func.now())
#     teammate_id = Column(Integer, ForeignKey("teammates.id"))
#     badge_id = Column(Integer, ForeignKey("badges.id"))

#     teammate = relationship("Teammates", back_populates="teammates", uselist=False)
#     badge = relationship("Badges", back_populates="badges", uselist=False)


# class CommentsHistoryTeammate(Base):
#     __tablename__ = "comments_hist_teammate"

#     id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     datetime = Column(DateTime, server_default=func.now())
#     teammate_id = Column(Integer, ForeignKey("teammates.id"))
#     comment = Column(String)

#     teammate = relationship("Teammates", back_populates="teammates", uselist=False)


# class CommentsHistoryDepartment(Base):
#     __tablename__ = "comments_hist_department"

#     id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     datetime = Column(DateTime, server_default=func.now())
#     department_id = Column(Integer, ForeignKey("departments.id"))
#     comment = Column(String)

#     department = relationship("Departments", back_populates="departments", uselist=False)


# class ScoreHistoryDepartment(Base):
#     __tablename__ = "score_hist_department"

#     id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     datetime = Column(DateTime, server_default=func.now())
#     score = Column(Float)
#     department_id = Column(Integer, ForeignKey("departments.id"))

#     department = relationship("Departments", back_populates="departments", uselist=False)


# class ScoreHistoryTeammate(Base):
#     __tablename__ = "score_hist_teammate"

#     id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     datetime = Column(DateTime, server_default=func.now())
#     score = Column(Float)
#     teammate_id = Column(Integer, ForeignKey("teammates.id"))

#     teammate = relationship("Teammates", back_populates="comments", uselist=False)
