
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,Session
from sqlalchemy import Text,Boolean,select

from engine import engine

#migration -> alter -> 
#SQL-> ALMEBIC

class Base(DeclarativeBase):
    pass

class Employee(Base):

    __tablename__="employee"

    #columns
    #colums static property 
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str]=mapped_column(Text,nullable=False)
    email:Mapped[str]=mapped_column(Text,nullable=False,unique=True)

#if table does not exit it will create it
Base.metadata.create_all(engine)

with Session(engine) as session:
    
    name="Ndovu3"
    email="ndovu3@gmail.com"

    st_employess=select(Employee)

    #execute
    results=session.scalars(st_employess).all()

    for emp in results:
        print(f"name: {emp.name}")

    #Creating DATA
    # emp=Employee(name=name,email=email)
    # session.add(emp)
    # session.commit()

    #READING DATA

    # UPDATE AND DELETE