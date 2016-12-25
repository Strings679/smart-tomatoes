import api
import smart_tomatoes

action_movies = 28
comedy_movies = 35

# Get a Movie by Genre ID. More about Genre IDs here: https://developers.themoviedb.org/3/genres
movies = api.GetMovie().search_by_genre(action_movies)
smart_tomatoes.open_movies_page(movies)  # Generate the Web Page with the results of the API
