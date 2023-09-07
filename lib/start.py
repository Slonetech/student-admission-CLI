from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Float, create_engine
from sqlalchemy.orm import relationship, sessionmaker,declarative_base



Base = declarative_base()
engine = create_engine('sqlite:///student.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    grades = relationship('Grade', backref='student')

    def __repr__(self):
        return f'<Student {self.name}>' 
    
    # @classmethod

# def get_all(cls):

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Float, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'))

    def __repr__(self):
        return f'<Grade {self.grade}>'

if __name__ == '__main__':
    pass