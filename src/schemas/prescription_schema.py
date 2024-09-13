from pydantic import BaseModel
from typing import List, Optional

class Prescription(BaseModel):
    id: Optional[int] = None
    medicalRecord: str
    name: str
    medicine: str
    unit: str
    dose: int
    via: str
    posology: str
    
class PrescriptionView(BaseModel):
    medicalRecord: str
    name: str
    medicine: str
    unit: str
    dose: int
    via: str
    posology: str
    