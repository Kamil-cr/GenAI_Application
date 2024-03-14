from sqlalchemy import create_engine, Column, Integer, String, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from dotenv import get_key

SQLALCHEMY_DATABASE_URL:str = str(get_key(".env", "DATABASE_URL"))

# Create a database file
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()