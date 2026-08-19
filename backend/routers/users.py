from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas
from crud import user
from services.auth import get_current_user
from models import User

router=APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserResponse)
def create_user(user_: schemas.UserCreate, db: Session = Depends(get_db)):
    return user.create_user(db, user_)

@router.get("/me", response_model=schemas.UserResponse)
def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user