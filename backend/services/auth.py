import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from database import get_db
from sqlalchemy.orm import Session
import models

load_dotenv()
SECRET_KEY=os.environ.get("SECRET_KEY")
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict):
    # Copy of the data
    to_encode=data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        #Extract the user ID
        user_id: str =  payload.get("sub")
        if user_id is None:
            raise credentials_exception

    # If the token is expired
    except jwt.InvalidTokenError:
        raise credentials_exception

    # Retrieve the verified user
    user = db.query(models.User).filter(models.User.id == int(user_id)).one_or_none()
    if user is None:
        raise credentials_exception

    return user    