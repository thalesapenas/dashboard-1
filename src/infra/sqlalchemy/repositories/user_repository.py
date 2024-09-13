from sqlalchemy.orm import Session
from src.schemas import user_schema
from src.infra.sqlalchemy.models import models

class User():
    
    def __init__(self,db: Session):
        self.db = db
    
    def create(self, user: user_schema.User): 
        db_user = models.User(      id = user.id,
                                    email=user.email,
                                    password=user.password,
                                    name = user.name
                                    )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def get_all(self):
        users = self.db.query(models.User).all()
        return users
    
    def verify_email(self, email:str):
        search = self.db.query(models.User).filter(models.User.email == email).first()
        return search
        
    def get(self):
        pass
    
    def remove(self):
        pass
    
    def update(self):
        pass
    