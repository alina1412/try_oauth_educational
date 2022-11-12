import datetime
from typing import Any, Optional

from fastapi import Depends, Request
from jose import JWTError
from passlib.context import CryptContext

from service.config import key
from service.exceptions.exceptions import CredentialsException
from service.oauth.headers import get_token_from_header, validate_bearer_type
from service.oauth.tokens import decode_token
from service.utils.fake_db import get_user


myctx = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])


def verify_password(user: Optional[dict], password: str) -> bool:
    password_in_db = user.get("password")
    return myctx.verify(password, password_in_db)


def verify_user(user: Optional[dict], password: str) -> bool:
    if not user:
        return False
    if not verify_password(user, password):
        return False
    return True


def validate_token(user: Optional[dict], expired_time: str) -> None:
    if (
        not user
        or expired_time is None
        or datetime.datetime.fromisoformat(expired_time) < datetime.datetime.utcnow()
    ):
        raise CredentialsException(detail="expired token")


def check_token(token: str) -> dict[str, Any]:
    """decode_token, get("username") from db of registered users, validate_token"""
    try:
        data: dict = decode_token(token, key)
        # Если токен валиден, то в data запишется содержимое claims.
        expired_time = data.get("expire", None)
        user = get_user(data.get("username", None))
    except JWTError as exc:
        raise CredentialsException(detail="Incorrect token") from exc

    try:
        validate_token(user, expired_time)
    except CredentialsException as exc:
        raise CredentialsException(detail=exc.detail) from exc

    return {"token": "valid", "claims": data, "token_type": "bearer"}


async def get_user_by_token(request: Request, _=Depends(validate_bearer_type)) -> dict:
    print(f"in function : {get_user_by_token.__name__}")
    token = get_token_from_header(request)
    if token is None:
        print("no 'client_secret' in a header")
        raise CredentialsException(detail="no 'client_secret' in a header")

    token_info = check_token(token)
    # token_info: {"token": "valid", "claims": data, "token_type": "bearer"}
    data = token_info.get("claims", {})
    return data
