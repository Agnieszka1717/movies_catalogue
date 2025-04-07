
import requests
from movies_catalogue import tmdb_client
from unittest.mock import Mock



def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url

def get_movies_list(list_type):
   endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
   headers = {
       "Authorization": f"Bearer {tmdb_client.API_TOKEN}"
   }
   response = requests.get(endpoint, headers=headers)
   response.raise_for_status()
   return response.json()

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_name="popular")
   assert movies_list is not None

def test_get_movies_list(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_name="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
   mock_single_movie = ['Movie']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie
   monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", requests_mock)
   single_movie = tmdb_client.get_single_movie(movie_id=1)
   assert single_movie == mock_single_movie


def test_get_single_movie_cast(monkeypatch):
   mock_single_movie_cast = {"cast":"test"}
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie_cast
   monkeypatch.setattr("movies_catalogue.tmdb_client.requests.get", requests_mock)
   single_movie_cast = tmdb_client.get_single_movie_cast(movie_id=1)
   assert single_movie_cast == mock_single_movie_cast["cast"]