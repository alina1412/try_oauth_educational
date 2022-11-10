import datetime
import json
from typing import Any, Dict, Optional
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
import jose
import uvicorn
from jose import jwt

load_dotenv()
from os import environ
key = environ.get("key")


fake_db = {
	"John Doe": {
		"user_name": "John Doe", 
		"password": "kcolsnrq", 
		"is_admin": True,
	},
	"bbb": {
		"user_name": "bbb", 
		"password": "mm38doc6", 
		"is_admin": False,
	},
}

app = FastAPI()

class CredentialsException(HTTPException):
    def __init__(self,  
                detail: Any = None, 
                headers: Optional[Dict[str, Any]] = None,
                status_code=status.HTTP_401_UNAUTHORIZED,) -> None:
        super().__init__(status_code, detail, headers)



def get_user(user_name) -> dict:
    return fake_db.get(user_name, {})


def verify_password(user, password) -> bool:
    password_in_db = user.get("password")
    if password_in_db == password:
        return True
    return False


def verify_user(user: dict, password: str) -> bool:
    if not user:
        return False
    if not verify_password(user, password):
        return False
    return True


def generate_token(user_name, key):
    """   """
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    expire = expire.isoformat()
    data_to_encode = {"user_name": user_name, "expire": expire}
    token = jwt.encode(
        claims=data_to_encode, 
        key=key,
    )
    return token

@app.post("/token/get", responses={
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
        CredentialsException().status_code: {},})
def get_token(user_name: str, password: str):
    """  Верифицировать пользователя, сопоставляя присланный password с паролем из fake_db
Генерировать токен и возвращать его пользователю.
"""
    assert key != None
    user = get_user(user_name)
    if not verify_user(user, password):
        raise CredentialsException(detail="Incorrect user_name or password",
        )
    token = generate_token(user_name, key)
    return {"token": token}



@app.post("/token/check", responses={
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
        CredentialsException().status_code: {},})
def check_token(token: str):
    """ Проверка токена"""
    try:
        data = jwt.decode(token, key)
        # Если токен валиден, то в data запишется содержимое claims.
    except jose.JWTError as exc:
        raise CredentialsException(detail="Incorrect token") from exc

    expired_time = data.get("expire", None)
    user = get_user(data.get("user_name", None))

    if not user or expired_time is None or datetime.datetime.fromisoformat(expired_time) < datetime.datetime.utcnow():
        raise CredentialsException(detail="expired token")

    return {
        "token": "valid",
        "claims": data
    }


if __name__ == "__main__":
    uvicorn.run("service.__main__:app", host="0.0.0.0", port=8000, reload=True)
