# tests/e2e/test_app.py
from httpx import AsyncClient
import pytest
from src.main import app


@pytest.mark.asyncio
async def test_movie_weather_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/movie-weather/?title=The Godfather")
        assert response.status_code == 200, "Debería devolver un código de estado 200"
        assert (
            "The Godfather" in response.text
        ), "Debería devolver los datos de la película y del clima"
