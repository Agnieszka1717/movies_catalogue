from unittest.mock import Mock
from main import app

def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular')

# def test_list(monkeypatch):
#    api_mock = Mock(return_value={'results': []})
#    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

#    with app.test_client() as client:
#        response = client.get('/')
#        assert response.status_code == 200
#        api_mock.assert_called_once_with('movie/popular')