from typing import Optional

from fastapi import Request

from service.exceptions.exceptions import CredentialsException


async def validate_bearer_type(request: Request) -> None:
    print(f"in function : {validate_bearer_type.__name__}")

    token_type: str = request.headers.get("Authorization")
    if not token_type:
        print("no 'Authorization' in a header")

    if not token_type or token_type.lower() != "bearer":
        print("CredentialsException")
        raise CredentialsException(detail="not type 'bearer' in a header")


def get_token_from_header(request: Request) -> str | None:
    token = request.headers.get("client_secret")
    return token
