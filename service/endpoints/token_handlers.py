from typing import Any

from fastapi import APIRouter, Depends, status

from service.config import key
from service.exceptions.exceptions import CredentialsException
from service.oauth.tokens import generate_token
from service.schemas.schemas import User
from service.utils.fake_db import get_user
from service.utils.utils import check_token, verify_user

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
def generate_token_handler(user_input: User = Depends()):
    """Верифицирует зфрегистрированного пользователя,
    сопоставляя присланный password с паролем из fake_db
    Генерирует токен и возвращает его пользователю."""
    assert key != None
    user = get_user(user_input.username)
    if not verify_user(user, user_input.password):
        raise CredentialsException(
            detail="Incorrect username or password",
        )
    token = generate_token(user_input.username, key)
    return {"token": token, "token_type": "bearer"}


@api_router.post(
    "/token/check",
    responses={
        CredentialsException().status_code: {},
    },
)
def check_token_handler(token: str):
    """Проверка существования и действительности токена"""
    token_data: dict[str, Any] = check_token(token)
    return token_data
