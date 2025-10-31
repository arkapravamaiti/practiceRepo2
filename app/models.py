from sqlalchemy import Column, Integer, String
from .database import Base

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department = Column(String, index=True)
    role = Column(String)
    email = Column(String, unique=True, index=True)
