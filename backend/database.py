from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import os

DATABASE_URL = os.getenv('DATABASE_URL')

def check_connection():
    try:
        connection = psycopg2.connect(DATABASE_URL)
        print("Connection to PostgreSQL server was successful!")
        connection.close()
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")

check_connection()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
