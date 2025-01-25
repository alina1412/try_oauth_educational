from datetime import datetime

from pydantic import BaseModel, Field


class UserShema(BaseModel):
    username: str = Field(description="unique username")
    password: str = Field(description="password")

    class Config:
        json_schema_extra = {"example": {"username": "joe", "password": "123"}}


class TokenOutputSchema(BaseModel):
    token: str = Field(description="token")
    token_type: str = Field(description="token_type")

    class Config:
        json_schema_extra = {
            "example": {
                "token": "kjnevonwbw..vwfb.eabae",
                "token_type": "bearer",
            }
        }


class TokenDataSchema(BaseModel):
    username: str = Field(description="username")
    expire: datetime = Field(description="expire datetime")


class TokenCheckedSchema(BaseModel):
    token: str = Field(description="token")
    claims: TokenDataSchema
    token_type: str = Field(description="token_type")


class InputFormSchema(BaseModel):
    client_secret: str = Field(
        description="client secret token",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "client_secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvZSIsImV4cGlyZSI6IjIwMjUtMDEtMjRUMTQ6Mjg6MDMuMDM2NzI0KzAwOjAwIn0.GTphQVoUy6eBX14hx2UPXv6-4u4tbrgUEWLEHXGLFho",
            }
        }
