import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#loading the variablse from .env
load_dotenv()

# Fetch the URL
DATABASE_URL= os.getenv("DATABASE_URL")

#Initializes the central communication for the database
engine = create_engine(DATABASE_URL)

# Factory for generating isolated database sessions per API request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class and central registry for all SQLAlchemy ORM models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()