from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

    
class User(Base):
    __tablename__= 'Users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)

    
class Prescription(Base):
    __tablename__= 'Prescriptions'
    
    id = Column(Integer, primary_key=True, index=True)
    medicalRecord = Column(String)
    name = Column(String)
    medicine = Column(String)
    unit = Column(String)
    dose = Column(Integer)
    via = Column(String)
    posology = Column(String)
