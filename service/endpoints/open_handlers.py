from typing import Optional

from fastapi import APIRouter, status

api_router = APIRouter(
    prefix="/v1",
    tags=["open"],
)


@api_router.get(
    "/open",
    responses={
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
    },
)
def look_open(username: str | None = None):
    """No token needed"""
    return {"OPEN Hello to all": username}
