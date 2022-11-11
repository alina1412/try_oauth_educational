from fastapi import APIRouter, status
from jose import JWTError

from service.config import key
from service.exceptions.exceptions import CredentialsException
from service.oauth.tokens import decode_token, generate_token
from service.utils.fake_db import get_user
from service.utils.utils import validate_token, verify_user

api_router = APIRouter(
    prefix="/v1",
    tags=["auth"],
)


@api_router.post(
    "/token/receive",
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
        CredentialsException().status_code: {},
    },
)
def generate_token_handler(user_name: str, password: str):
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
def check_token_handler(token: str):
    """Проверка токена"""
    try:
        data = decode_token(token, key)
        # Если токен валиден, то в data запишется содержимое claims.
        expired_time = data.get("expire", None)
        user = get_user(data.get("username", None))
    except JWTError as exc:
        raise CredentialsException(detail="Incorrect token") from exc

    try:
        validate_token(user, expired_time)
    except CredentialsException as exc:
        raise CredentialsException(detail="Incorrect token") from exc

    return {"token": "valid", "claims": data}
