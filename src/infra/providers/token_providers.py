from datetime import datetime, timedelta
from jose import jwt

#config
SECRET_KEY = "99a29dc8105fd2fa39d8cdc04733938d"
ALGORITHM = "HS256"
EXPIRES_IN_MINUTES = 300


def create_acess_token(data: dict):
    data = data.copy()
    expiration =  datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MINUTES)
    
    data.update({"exp": expiration})
    
    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    
    return token_jwt



def verify_acess_token(token: str):
    package = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    
    return package.get("sub")
