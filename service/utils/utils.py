import datetime
from typing import Any, Optional

from fastapi import Depends, Request
from jose import JWTError

from service.config import key
from service.exceptions.exceptions import CredentialsException
from service.oauth.headers import get_token_from_header, is_bearer
from service.oauth.tokens import decode_token
from service.utils.fake_db import get_user


def verify_password(user: Optional[dict], password: str) -> bool:
    password_in_db = user.get("password")
    if password_in_db == password:
        return True
    return False


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


async def get_user_by_token(request: Request, bearer=Depends(is_bearer)) -> dict:
    print(f"in function : {get_user_by_token.__name__}")
    token = get_token_from_header(request)
    if token is None:
        print("no 'client_secret' in a header")
        raise CredentialsException(detail="no 'client_secret' in a header")

    token_info = check_token(token)
    # token_info: {"token": "valid", "claims": data, "token_type": "bearer"}
    data = token_info.get("claims", {})
    return data
