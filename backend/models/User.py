from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email=Column(String, unique=True, index=True)
    hashed_password=Column(String)

    expenses = relationship("Expense", back_populates="owner")