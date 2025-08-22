from dotenv import load_dotenv
import os

#Load .env variables

load_dotenv()

drivername=os.getenv("drivername")

print(drivername)