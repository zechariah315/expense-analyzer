from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from models import Expense
import schemas

def create_user_expense(db: Session, expense: schemas.ExpenseCreate, user_id: int):
    db_expense = Expense(**expense.model_dump(), owner_id=user_id)
    db.add(db_expense)

    try:
        db.commit()
        db.refresh(db_expense)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=404, detail="User not found. cannot add expense.")
    return db_expense

def get_expenses_by_user(db: Session, user_id: int, skip: int=0, limit=100):
    return db.query(Expense).filter(Expense.owner_id==user_id).order_by(Expense.date.desc()).offset(skip).limit(limit).all()

