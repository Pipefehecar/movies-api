import os
import requests

API_KEY = os.getenv("API_KEY_TMDB")

def fetch_movie_data(title: str) -> dict | None:
    """Fetch movie data from The Movie Database API"""

    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
        ).json()
        return response["results"][0]
    except Exception as e:
        print(e)
        return None


def fetch_weather_data(date: str)-> dict:
    """Fetch weather data from Open-Meteo API"""

    # Barranquilla, Colombia coordinates
    latitude = 11.004107
    longitude = -74.806981

    try:
        response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start={date}&end={date}"
        )
        return response.json()
    except Exception as e:
        print(e)
        return None

