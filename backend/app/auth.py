from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET_KEY = "abcdabcd"
ALGORITHM = "HS256"

security = HTTPBearer()
auth_router = APIRouter()

@auth_router.post("/login")
def login():
    payload = {
        "user": "admin",
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token}


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
