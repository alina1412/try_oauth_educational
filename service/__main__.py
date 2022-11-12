import uvicorn
from fastapi import FastAPI

from service.endpoints.private_handlers import api_router as private_route
from service.endpoints.token_handlers import api_router as token_routes
from service.endpoints.open_handlers import api_router as open_routes

app = FastAPI()

app.include_router(private_route)
app.include_router(token_routes, prefix="/auth")
app.include_router(open_routes)


if __name__ == "__main__":
    uvicorn.run("service.__main__:app", host="0.0.0.0", port=8000, reload=True)
