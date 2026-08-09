from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# -------------------
# User Schemas
# -------------------
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# -------------------
# Expense Schemas
# -------------------

class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: Optional[str] = None

class ExpenseResponse(ExpenseCreate):
    id: int
    date: datetime
    owner_id: int

    class Config:
        from_attributes = True


# -------------------
# Token Schemas
# ------------------
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]=None