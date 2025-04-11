import requests
import os
API_TOKEN = os.environ["tmdb_token"]

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_popular_movies():
    return call_tmdb_api("movie/popular")

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")["cast"]

def get_movies_list(list_name="popular"):
    return call_tmdb_api(f"movie/{list_name}")

def get_movies(how_many, list_name):
    data = get_movies_list(list_name)
    return data["results"][:how_many]

def get_poster_url(poster_path, size="w342"):
    url = "https://image.tmdb.org/t/p/" + size + "/" + poster_path 
    return url 
