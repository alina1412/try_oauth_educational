from fastapi import APIRouter, Depends, status

from service.exceptions.exceptions import CredentialsException
from service.oauth.token_manager import TokenManager
from service.schemas.schemas import (
    TokenCheckedSchema,
    TokenOutputSchema,
    UserShema,
)
from service.utils.fake_db import get_user
from service.utils.utils import verify_user

api_router = APIRouter(
    prefix="/v1",
    tags=["auth"],
)


@api_router.post(
    "/token/get",
    response_model=TokenOutputSchema,
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
        CredentialsException().status_code: {},
    },
)
def generate_token_handler(user_input: UserShema = Depends()):
    """Верифицирует зфрегистрированного пользователя,
    сопоставляя присланный password с паролем из fake_db
    Генерирует токен и возвращает его пользователю."""
    user = get_user(user_input.username)
    if not verify_user(user, user_input.password):
        raise CredentialsException(
            detail="Incorrect username or password",
        )
    token = TokenManager().generate_token(user_input.username)
    return {"token": token, "token_type": "bearer"}


@api_router.post(
    "/token/check",
    response_model=TokenCheckedSchema,
    responses={
        CredentialsException().status_code: {},
    },
)
def check_token_handler(token: str):
    """Проверка существования и действительности токена"""
    token_data = TokenManager().check_token(token)
    return token_data
