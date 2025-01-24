from fastapi import APIRouter, Depends, status

from service.exceptions.exceptions import CredentialsException
from service.schemas.schemas import User
from service.utils.fake_db import get_user
from service.utils.utils import get_user_token_data, verify_user

api_router = APIRouter(
    prefix="/v1",
    tags=["private"],
)


@api_router.post(
    "/",
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"description": "Bad request"},
        CredentialsException().status_code: {},
    },
)
def private_page(
    user_input: User = Depends(),
    user_token_data=Depends(get_user_token_data),
):
    """Page can be seen if user registered and
    header has  -H 'Authorization:bearer' and
    -H 'client_secret:<user-token>"""
    user = get_user(user_input.username)
    if not verify_user(user, user_input.password):
        raise CredentialsException
    return {"Hello": user_input.username, "data": user_token_data}
