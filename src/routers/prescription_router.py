from fastapi import  Depends, status, APIRouter, HTTPException
from src.schemas import prescription_schema, user_schema
from src.infra.sqlalchemy.repositories import prescription_repository
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.routers.utilitaries_router import get_logged_user

router = APIRouter(prefix="/prescription", tags=["Prescription"])

@router.post("/create", status_code=status.HTTP_201_CREATED,response_model=prescription_schema.Prescription) 
def create( prescription: prescription_schema.Prescription, user: user_schema.userLogin = Depends(get_logged_user), db: Session = Depends(get_db)):

    created_prescription = prescription_repository.Prescription(db).create(prescription)
    
    return created_prescription
    
    
    
@router.get("", status_code=status.HTTP_200_OK) 
def get_all(user: user_schema.userLogin = Depends(get_logged_user), db: Session = Depends(get_db)):

    prescriptions = prescription_repository.Prescription(db).get_all()
    
    return prescriptions