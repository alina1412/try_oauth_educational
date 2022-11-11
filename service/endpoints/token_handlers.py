import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, status
from jose import JWTError

from service.config import key
from service.exceptions.exceptions import CredentialsException
from service.oauth.tokens import decode_token, generate_token
from service.utils.fake_db import fake_db, get_user
from service.utils.utils import verify_password, verify_user

api_router = APIRouter(
    prefix="/v1",
    tags=["auth"],
)


@api_router.post(
    "/token/get",
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
        CredentialsException().status_code: {},
    },
)
def get_token(user_name: str, password: str):
    """Верифицировать пользователя, сопоставляя присланный password с паролем из fake_db
    Генерировать токен и возвращать его пользователю."""
    assert key != None
    user = get_user(user_name)
    if not verify_user(user, password):
        raise CredentialsException(
            detail="Incorrect user_name or password",
        )
    token = generate_token(user_name, key)
    return {"token": token}


@api_router.post(
    "/token/check",
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
        CredentialsException().status_code: {},
    },
)
def check_token(token: str):
    """Проверка токена"""
    try:
        data = decode_token(token, key)
        # Если токен валиден, то в data запишется содержимое claims.
    except JWTError as exc:
        raise CredentialsException(detail="Incorrect token") from exc

    expired_time = data.get("expire", None)
    user = get_user(data.get("user_name", None))

    if (
        not user
        or expired_time is None
        or datetime.datetime.fromisoformat(expired_time) < datetime.datetime.utcnow()
    ):
        raise CredentialsException(detail="expired token")

    return {"token": "valid", "claims": data}
