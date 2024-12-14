from fastapi import APIRouter
from src.services.providers import fetch_movie_data, fetch_weather_data
from src.schemas.movie_weather import MovieWeather, Movie, WeatherData

router = APIRouter()


@router.get("/movie-weather/", response_model=MovieWeather)
def get_movie_weather(title: str) -> dict[str, str] | MovieWeather:  
    if not title:
        return {"error": "Movie title is required"}
    
    movie_data: dict = fetch_movie_data(title)
    if not movie_data:
        return {"error": "Movie not found"}

    weather_data: dict = fetch_weather_data(movie_data["release_date"])
    return MovieWeather(movie=Movie(**movie_data), weather=WeatherData(**weather_data))
