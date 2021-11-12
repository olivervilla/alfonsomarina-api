from fastapi import FastAPI, HTTPException, Depends
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


@app.post("/users/", response_model=models.Teammate)
async def create_user(user: models.TeammateCreate, db: Session = Depends(get_db)):
    db_user = crud.get_teammate(db, user_id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User code already registered")
    return crud.create_teammate(db, user)


@app.get("/users/{user_id}", response_model=models.Teammate)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_teammate(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/departments/", response_model=models.Department)
async def create_department(department: models.DepartmentCreate, db: Session = Depends(get_db)):
    db_department = crud.get_departament_by_name(db, departament_name=department.name)
    if db_department:
        raise HTTPException(status_code=400, detail="Department already registered")
    return crud.create_department(db, department)


@app.get("/departments/{department_id}", response_model=models.Department)
async def read_user(department_id: int, db: Session = Depends(get_db)):
    db_department = crud.get_departament(db, department_id=department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
