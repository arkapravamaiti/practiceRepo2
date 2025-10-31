from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from .database import get_db, Base, engine
from .models import Employee

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/employees/", response_model=List[dict])
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = db.query(Employee).offset(skip).limit(limit).all()
    return [{"id": emp.id, "name": emp.name, "department": emp.department, "role": emp.role, "email": emp.email} for emp in employees]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
