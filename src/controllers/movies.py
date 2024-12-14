from fastapi import APIRouter
from src.schemas.movie_weather import MovieWeather
from src.services.movies import get_movie_weather_data
from fastapi import HTTPException

router = APIRouter()

@router.get("/movie-weather/", response_model=MovieWeather)
def get_movie_weather(title: str) -> MovieWeather:
    if not title:
        raise HTTPException(status_code=400, detail="Movie title is required")

    try:
        return get_movie_weather_data(title)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
