from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas
from crud import user

router=APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserResponse)
def create_user(user_: schemas.UserCreate, db: Session = Depends(get_db)):
    return user.create_user(db, user_)

