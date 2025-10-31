from .database import SessionLocal, engine, Base
from .models import Employee
from faker import Faker

def setup_database():
    # Create database tables
    Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    fake = Faker()
    
    # Check if data already exists
    if db.query(Employee).count() == 0:
        # Create and add 50 fake employees
        for _ in range(50):
            employee = Employee(
                name=fake.name(),
                department=fake.job(),
                role=fake.job(),
                email=fake.email()
            )
            db.add(employee)
        db.commit()
        print("Added 50 fake employees to the database.")
    else:
        print("Database already contains data. Skipping seed.")
    
    db.close()

if __name__ == "__main__":
    setup_database()
    seed_data()
