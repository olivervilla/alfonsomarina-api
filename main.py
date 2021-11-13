from fastapi import FastAPI, HTTPException, Depends
from typing import List
import crud, models, schemas
import uvicorn

from database import SessionLocal, engine

from sqlalchemy.orm import Session

schemas.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------
#   TEAMMATE / USER
# ---------------------------------------------
@app.post("/users/", response_model=models.Teammate)
async def create_user(user: models.TeammateCreate, db: Session = Depends(get_db)):
    db_user = crud.read_teammate(db, user_id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User code already registered")
    return crud.create_teammate(db, user)


@app.get("/users/", response_model=List[models.Teammate])
async def get_user_all(db: Session = Depends(get_db)):
    return crud.read_teammate_all(db)


@app.get("/users/{user_id}", response_model=models.Teammate)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.read_teammate(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/users/{user_id}", response_model=models.Teammate)
async def update_user(user: models.TeammateUpdate, user_id: int, db: Session = Depends(get_db)):
    db_user = crud.update_teammate(db, user, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}") # response_model=models.Teammate
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    if crud.delete_teammate(db, user_id):
        return {}
    else:
        raise HTTPException(status_code=404, detail="User not found")


# ---------------------------------------------
#   DEPARTMENT
# ---------------------------------------------
@app.post("/departments/", response_model=models.Department)
async def create_department(department: models.DepartmentCreate, db: Session = Depends(get_db)):
    db_department = crud.read_department_by_name(db, department_name=department.name)
    if db_department:
        raise HTTPException(status_code=400, detail="Department already registered")
    return crud.create_department(db, department)


@app.get("/departments/", response_model=List[models.Department])
async def get_department_all(db: Session = Depends(get_db)):
    return crud.read_department_all(db)


@app.get("/departments/{department_id}", response_model=models.Department)
async def get_department(department_id: int, db: Session = Depends(get_db)):
    db_department = crud.read_department(db, department_id=department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department


@app.put("/departments/{department_id}", response_model=models.Department)
async def update_department(department: models.DepartmentUpdate, department_id: int, db: Session = Depends(get_db)):
    db_department = crud.update_department(db, department, department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department


@app.delete("/departments/{department_id}") # response_model=models.Department
async def delete_department(department_id: int, db: Session = Depends(get_db)):
    if crud.delete_department(db, department_id):
        return {}
    else:
        raise HTTPException(status_code=404, detail="Department not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
