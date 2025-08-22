#File for connecting to  our db
from sqlalchemy import create_engine,text
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base,sessionmaker


db_credentials={
    "drivername":"postgresql+psycopg",
    "host":"aws-1-ap-southeast-1.pooler.supabase.com",
    "username":"postgres.hligqmxuekndtvcxuxrr",
    "password":"AfQxlUVjojzIjh5g",
    "port":5432,
    "database":"postgres"
}

#BUILD URL
DATABASE_URL=URL.create(**db_credentials)

engine=create_engine(DATABASE_URL,echo=True,future=True)


SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

#BASE
Base=declarative_base()