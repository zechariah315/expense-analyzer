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

def update_expense(db: Session, expense_id: int, user_id: int, expense_data: schemas.ExpenseUpdate):
    
    db_expense=db.query(Expense).filter(Expense.id==expense_id, Expense.owner_id==user_id).one_or_none()

    if not db_expense:
        return None
    
    update_data=expense_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_expense, key, value)

    db.commit()
    db.refresh(db_expense)
    return db_expense

def delete_expense(db: Session, expense_id: int, user_id):

    db_expense=db.query(Expense).filter(Expense.id==expense_id, Expense.owner_id==user_id).one_or_none()

    if not db_expense:
        return None

    db.delete(db_expense)
    db.commit()
    return db_expense