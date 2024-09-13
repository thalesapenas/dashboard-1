from fastapi import  Depends, status, APIRouter, HTTPException
from src.schemas import user_schema
from src.infra.sqlalchemy.repositories import user_repository 
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import hash_providers, token_providers
from src.routers.utilitaries_router import get_logged_user

router = APIRouter(prefix="/auth", tags=["User"])

@router.post("/signup", status_code=status.HTTP_201_CREATED,response_model=user_schema.UserView) 
def sign_up(user: user_schema.User, db: Session = Depends(get_db)):
    
    verify_user = user_repository.User(db).verify_email(user.email)
    if verify_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already registered")
    
    user.password = hash_providers.generate_hash(user.password)
    
    created_user = user_repository.User(db).create(user)

    return created_user


@router.post("/singin", status_code=status.HTTP_200_OK, response_model=user_schema.userLoginSuccess)
def sing_in (user_login :user_schema.userLogin, db: Session = Depends(get_db)):
    password = user_login.password
    email = user_login.email
    
    #verificar se o usuário existe
    user = user_repository.User(db).verify_email(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found") 
    
    #verificar se a senha é válida
    valid_password = hash_providers.verify_hash(password, user.password)
    if not valid_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")


    TOKEN = token_providers.create_acess_token({"sub": user.email})
    
    return user_schema.userLoginSuccess(user=user_schema.UserView(id=user.id, email=user.email, name = user.name), token=TOKEN)

#só chamo a funcao que verifica o token e retorna o respectivo usuario do token
@router.get("/me", status_code=status.HTTP_200_OK,response_model=user_schema.UserView)
def me (user: user_schema.userLogin = Depends(get_logged_user)):
    return user

#criar endpoint para prescrição