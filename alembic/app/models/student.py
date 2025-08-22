from app import Base

from sqlalchemy import Column,String,BIGINT

class Student(Base):

    __tablename__="student"

    id=Column(BIGINT,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)
