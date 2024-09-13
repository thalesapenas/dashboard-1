from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: Optional[int] = None
    email: str
    password: str
    name: str
    

class UserView(BaseModel):
    email: str
    name: str

class userLogin(BaseModel):
    password: str
    email: str
    
class userLoginSuccess(BaseModel):
    user: UserView
    token: str
    