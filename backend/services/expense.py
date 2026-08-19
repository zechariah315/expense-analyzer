from fastapi import HTTPException, status

from models import Expense

def Not_found_expense_error(expense: Expense):
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found or unauthorized to modify")