from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import schemas
from crud import expense

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/{user_id}", response_model=schemas.ExpenseResponse)
def create_expense(user_id: int, expense_: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return expense.create_user_expense(db, expense_, user_id)

@router.get("/{user_id}", response_model=List[schemas.ExpenseResponse])
def read_expenses(user_id: int, skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return expense.get_expenses_by_user(db, user_id, skip, limit)