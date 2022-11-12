from fastapi import APIRouter, Depends, status

from service.exceptions.exceptions import CredentialsException
from service.schemas.schemas import User
from service.utils.utils import get_current_user

api_router = APIRouter(
    prefix="/v1",
    tags=["private"],
)


@api_router.post(
    "/",
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
        CredentialsException().status_code: {},
    },
)
def get_private(
    user_input: User = Depends(),
    user_token_data=Depends(get_current_user),
):
    """Page can be seen if  header has
    -H 'Authorization:bearer'
    -H 'client_secret:<user-token>"""
    return {"Hello": user_input.username, "data": user_token_data}
