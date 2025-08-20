from db import PG

class Employee():

    def __init__(self):
        pg=PG()
        
        query="""
            CREATE TABLE IF NOT EXISTS employee(
              id BIGSERIAL PRIMARY KEY,
              name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE
            )
        """
        pg.pg_query(query=query)
    
    def add(self,name,email):
        pg=PG()
        query="""
          INSERT INTO employee
          (name,email)
          VALUES  (%s,%s)
        """

        pg.pg_query(query=query,params=(name,email))
    
    

emp1=Employee()

#create an employee (C)
#all employees (R)
#Update 
#Delete
# emp1.add(name="Marry",email="marry@gmail.com")

while True:
    name=input("Enter employee name:")
    email=input("Enter employee email:")
    emp1.add(name=name,email=email)

    print("Employee added ")
    print("")
    another=input("Enter y to add another ?:")
    if another=="y" or another=="Y":
        continue
    break

# READ, READ. UPDATE()