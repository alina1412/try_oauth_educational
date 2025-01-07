import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from service.endpoints.open_handlers import api_router as open_routes
from service.endpoints.private_handlers import api_router as private_route
from service.endpoints.token_handlers import api_router as token_routes

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        },
        "apiKey": {
            "type": "apiKey",
            "name": "client_secret",
            "in": "header",
            "scheme": "apiKey",
        },
    }
    openapi_schema["security"] = [
        {"bearerAuth": ["read", "write"], "apiKey": ["read", "write"]}
    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.include_router(private_route)
app.include_router(token_routes, prefix="/auth")
app.include_router(open_routes)
app.openapi = custom_openapi


if __name__ == "__main__":
    uvicorn.run("service.__main__:app", host="0.0.0.0", port=8000, reload=True)
