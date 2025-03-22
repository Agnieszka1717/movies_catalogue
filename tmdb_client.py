import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "test"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_path, size="w342"):
    url = "https://image.tmdb.org/t/p/" + size + "/" + poster_path 
    return url 

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

