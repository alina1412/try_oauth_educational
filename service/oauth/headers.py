from typing import Optional

from fastapi import Request

from service.exceptions.exceptions import CredentialsException


async def is_bearer(request: Request) -> Optional[str]:
    print("in function : is_bearer")

    token_type: str = request.headers.get("Authorization")
    if not token_type:
        print("is_bearer: no 'Authorization' in a header")

    if not token_type or token_type.lower() != "bearer":
        print("is_bearer: CredentialsException")
        raise CredentialsException


def get_token_from_header(request: Request) -> str | None:
    token = request.headers.get("client_secret")
    return token
