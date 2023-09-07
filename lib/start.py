from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Float, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
engine = create_engine('sqlite:///student.db')
Session = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    subjects = relationship('Subject', backref='student')
    grades = relationship('Grade', backref='student')

    def __repr__(self):
        return f'<Student {self.name}>' 

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subject = Column(String(50), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'))

    def __repr__(self):
        return f'<Subject {self.subject}>'

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Float, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))

    def __repr__(self):
        return f'<Grade {self.grade}>'
