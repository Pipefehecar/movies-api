# tests/integration/test_movie_weather_service.py
from unittest.mock import patch
from src.services.movies import get_movie_weather_data


@patch("src.services.movies.fetch_movie_data")
@patch("src.services.movies.fetch_weather_data")
@patch("src.services.movies.send_to_webhook")
def test_get_movie_weather_data( mock_weather_data, mock_movie_data):
    mock_movie_data.return_value = {
        "title": "The Godfather",
        "release_date": "1972-03-14",
    }
    mock_weather_data.return_value = {"temperature": 20}
    movie_weather = get_movie_weather_data("The Godfather")
    assert (
        movie_weather.movie.title == "The Godfather"
    ), "Debería crear el objeto MovieWeather correctamente"
