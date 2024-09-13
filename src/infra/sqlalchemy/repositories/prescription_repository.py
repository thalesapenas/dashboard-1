from sqlalchemy.orm import Session
from src.schemas import  prescription_schema
from src.infra.sqlalchemy.models import models

class Prescription():
    
    def __init__(self,db: Session):
        self.db = db
    
    def create(self, prescription: prescription_schema.Prescription): 
        db_prescription = models.Prescription(  id = prescription.id,
                                                medicalRecord=prescription.medicalRecord,
                                                name = prescription.name,
                                                medicine = prescription.medicine,
                                                unit = prescription.unit,
                                                dose = prescription.dose,
                                                via = prescription.via,
                                                posology = prescription.posology)
        
        self.db.add(db_prescription)
        self.db.commit()
        self.db.refresh(db_prescription)
        return db_prescription
    
    def get_all(self):
        prescriptions = self.db.query(models.Prescription).all()
        
        return prescriptions
