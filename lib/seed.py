from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from start import Student, Subject, Grade, Base  # Replace 'start' with the actual module name where models are defined
from sqlalchemy.orm import registry
mapper_registry = registry()
fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///student.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear old data
    session.query(Student).delete()
    session.query(Subject).delete()
    session.query(Grade).delete()
    session.commit()

    print("Seeding students...")

    students = [
        Student(
            name=fake.name(),
            email=fake.email()
        )
        for i in range(10)
    ]

    session.add_all(students)
    session.commit()  # Commit the students to get valid IDs

    print("Seeding subjects...")
    subject_list = ["math", "comp sci", "english", "history"]
    subjects = [
        Subject(
            subject=random.choice(subject_list),
            student_id=random.choice(students).id
        )
        for i in range(30)
    ]

    session.add_all(subjects)
    session.commit()  # Commit the subjects to get valid IDs

    print("Seeding grades...")


    grades = [
        Grade(
            grade=random.randint(1, 100),
            student_id=random.choice(students).id,
            subject_id=random.choice(subjects).id
        )
        for i in range(100)
    ]

    session.add_all(grades)

    try:
        session.commit()
        print("Data committed successfully.")
    except Exception as e:
        session.rollback()
        print("Error committing data:", e)