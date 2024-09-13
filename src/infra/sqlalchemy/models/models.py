from sqlalchemy import Column, Integer, String
from src.infra.sqlalchemy.config.database import Base

    
class User(Base):
    __tablename__= 'Users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)

