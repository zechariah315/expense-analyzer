from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import schemas
from crud import expense
from services.auth import get_current_user
from models import User


router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/", response_model=schemas.ExpenseResponse)
def create_expense(expense_: schemas.ExpenseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return expense.create_user_expense(db, expense_, user_id=current_user.id)

@router.get("/", response_model=List[schemas.ExpenseResponse])
def read_expenses(skip: int=0, limit: int=100, db: Session=Depends(get_db), current_user: User=Depends(get_current_user)):
    return expense.get_expenses_by_user(db, skip=skip, limit=limit, user_id=current_user.id)