from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import func
from database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key = True)
    amount = Column(Float)
    category=Column(String, index=True)
    description=Column(String)
    date=Column(DateTime, default=func.now(), index=True)
    owner_id=Column(Integer, ForeignKey("users.id"), index=True)

    owner = relationship("User", back_populates="expenses")