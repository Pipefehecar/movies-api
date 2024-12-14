from fastapi import FastAPI
from src.controllers.movies import router as movie_router

app = FastAPI(
    title="Movie Weather API",
    description="Get weather data for a movie release date",
    version="0.1",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

app.include_router(movie_router, prefix="/api/v1")

