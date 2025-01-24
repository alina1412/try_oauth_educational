from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(description="unique username")
    password: str = Field(description="password")

    class Config:
        json_schema_extra = {"example": {"username": "joe", "password": "123"}}


class InputForm(User):
    client_secret: str = Field(
        description="client secret token",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "client_secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvZSIsImV4cGlyZSI6IjIwMjUtMDEtMjRUMTQ6Mjg6MDMuMDM2NzI0KzAwOjAwIn0.GTphQVoUy6eBX14hx2UPXv6-4u4tbrgUEWLEHXGLFho",
            }
        }
