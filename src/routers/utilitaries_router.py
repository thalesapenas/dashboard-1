from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException,status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_providers
from jose import JWTError
from src.infra.sqlalchemy.repositories import user_repository

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


def get_logged_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    try:
        email = token_providers.verify_acess_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    user = user_repository.User(db).verify_email(email)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user
    