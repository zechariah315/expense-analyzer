from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import schemas
from crud import expense
from services.auth import get_current_user
from models import User
from services.expense import Not_found_expense_error


router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/", response_model=schemas.ExpenseResponse)
def create_expense(expense_: schemas.ExpenseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return expense.create_user_expense(db, expense_, user_id=current_user.id)

@router.get("/", response_model=List[schemas.ExpenseResponse])
def read_expenses(skip: int=0, limit: int=100, db: Session=Depends(get_db), current_user: User=Depends(get_current_user)):
    return expense.get_expenses_by_user(db, skip=skip, limit=limit, user_id=current_user.id)

@router.get("/summary", response_model=List[schemas.CategorySummary])
def read_expense_summary(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Returns a calculated breakdown of total expenses grouped by category
    """
    return expense.get_eepense_summary_by_category(db, user_id=current_user.id)

@router.update("/{expese_id}", reponse_model=schemas.ExpenseResponse)
def update_expense(expense_id: int, expense_data: schemas.ExpenseUpdate, db: Session = Depends(get_db), current_user: User=Depends(get_current_user)):
    updated_expense=expense.update_expense(db, expense_id, current_user.id, expense_data)

    Not_found_expense_error(updated_expense)

    return updated_expense 

@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense_endpoint(expense_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    deleted_expense = expense.delete_expense(db, expense_id=expense_id, user_id=current_user.id)
    Not_found_expense_error(deleted_expense)
    return None