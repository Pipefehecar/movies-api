import os

import requests

from src.schemas.movie_weather import Movie, MovieWeather, WeatherData
from src.services.providers import fetch_movie_data, fetch_weather_data


def send_to_webhook(data: dict) -> int:
    """Send data to a webhook"""

    try:
        webhook_url = os.getenv("WEBHOOK_URL")
        response = requests.post(webhook_url, json=data)
        return response.status_code
    except Exception as e:
        raise ValueError("Webhook error: " + str(e))



def get_movie_weather_data(title: str) -> MovieWeather:
    """Get movie and weather data"""

    movie_data = fetch_movie_data(title)
    if not movie_data:
        raise ValueError("Movie not found")

    weather_data = fetch_weather_data(movie_data["release_date"])
    combined_data = MovieWeather(
        movie=Movie(**movie_data), weather=WeatherData(**weather_data)
    )

    send_to_webhook(combined_data.dict())

    return combined_data
