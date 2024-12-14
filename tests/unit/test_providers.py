# tests/unit/test_providers.py
from unittest.mock import patch
import pytest
from src.services.providers import fetch_movie_data


@patch("src.services.providers.requests.get")
def test_fetch_movie_data(mock_get):
    mock_get.return_value.json.return_value = {"results": [{"id": 1}]}
    result = fetch_movie_data("The Godfather")
    assert result == {
        "id": 1
    }, "Debería devolver los datos de la película correctamente"
