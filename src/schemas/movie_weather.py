from pydantic import BaseModel
from typing import List
from src.schemas.movies import Movie
from src.schemas.weather import WeatherData

class MovieWeather(BaseModel):
    movie: Movie
    weather: WeatherData
