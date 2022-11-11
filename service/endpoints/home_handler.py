from fastapi import APIRouter, Depends, Request, status

from service.exceptions.exceptions import CredentialsException

api_router = APIRouter(
    prefix="/v1",
    tags=["home"],
)


@api_router.get(
    "/",
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
        CredentialsException().status_code: {},
    },
)
def get_homepage(user_name: str, password: str):
    """"""
    return {"Hello": user_name}
