from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(example="joe", description="unique username")
    password: str = Field(example="123", description="password")


class InputForm(User):
    client_secret: str = Field(
        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvZSIsImV4cGlyZSI6IjIwMjItMTEtMTJUMDY6MjM6MzUuNTU2MTkxIn0.fgW0JVSrmIlJsf80WRtTfuW8wRiWNoGMhgQEZg_cTRg",
        description="client secret token",
    )
