import uvicorn
from fastapi import FastAPI

from service.endpoints.home_handler import api_router as home_route
from service.endpoints.token_handlers import api_router as token_routes

app = FastAPI()

app.include_router(home_route)
app.include_router(token_routes, prefix="/auth")


if __name__ == "__main__":
    uvicorn.run("service.__main__:app", host="0.0.0.0", port=8000, reload=True)
