from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from models import User
import schemas

password_hash = PasswordHash.recommended()

def get_password_hash(password: str):
    return password_hash.hash(password)

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):

    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)

    # Create the database model instance
    db_user = User(email=user.email, name=user.name, hashed_password=hashed_password)

    # Add it to the database and save
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return db_user


