from sqlalchemy import create_engine, Column, Integer, String, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

SQLALCHEMY_DATABASE_URL = "postgresql://kamilzafar54:0ubRWJhPZt3X@ep-silent-dust-a5r01rvj.us-east-2.aws.neon.tech/testdb?sslmode=require"

# Create a database file
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()