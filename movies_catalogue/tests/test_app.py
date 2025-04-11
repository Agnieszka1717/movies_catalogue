from unittest.mock import Mock

import pytest
from main import app

def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/upcoming')

@pytest.mark.parametrize('list_name', 
  ["now_playing", "popular", "top_rated", "upcoming"]
)
def test_list(monkeypatch, list_name):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get(f'/?list_name={list_name}')
       assert response.status_code == 200
       api_mock.assert_called_once_with(f'movie/{list_name}')