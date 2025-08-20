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

emp1=Employee()