from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from services.user import verify_password
from services.auth import create_access_token
from crud import user
import schemas

router = APIRouter(tags=["Authentication"])

@router.post("/login", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    db_user=user.get_user_by_email(db, email=form_data.username)

    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                        detail="Incorrect email or password",
                                        headers={"WWW-Authenticate": "Bearer"})

    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise credentials_exception

    access_token=create_access_token(data={"sub": str(db_user.id)})

    return {"access_token": access_token, "token_type": "bearer"}
