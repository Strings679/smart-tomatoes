import requests


class GetMovie:
    """
    This class allows you to GetMovies from the website "The Movie Database".
    In order for it to work, it is necessary to insert your API key on the __init__ function.
    You can get an API key at: https://www.themoviedb.org/documentation/api

    Through the method search_by_genre you can pass the Genre ID and get the following information from 20 movies:
        - Movie ID
        - Movie Title
        - Movie Poster Image
        - Movie Youtube Key
    """

    def __init__(self):
        self.parameters = {
            "api_key": '<<YOUR-API-KEY-HERE>>'  # Insert your API Key here
        }

    # Search by Genre method.
    def search_by_genre(self, genre):
        self.parameters["with_genres"] = genre  # Add the Genre to the Params

        # API Request to get 20 Movies from the Passed Genre ID.
        response = requests.get('https://api.themoviedb.org/3/discover/movie', params=self.parameters)
        data = response.json().get('results')
        movies = []  # List of Movies to be returned.

        # The count here and inside the For loop is to have a status indicator of the request progress.
        count = 0
        for full_movie in data:  # Loop over every movie found.
            count += 1
            print('Getting Movie ' + str(count) + ' of 20. Progress: ' + str((count / 20.) * 100) + '%')

            # Since the Video Trailer is not included in the first request, make another request with the movie ID
            # to get the Movie Videos and extract its trailer.
            get_video = requests.get('https://api.themoviedb.org/3/movie/' + str(full_movie.get('id')) + '/videos',
                                     params=self.parameters).json().get('results')

            # This is to prevent some Movies that don't have any videos from throwing an Error.
            if len(get_video) > 0:
                movie_trailer = get_video[0]  # Get the first video of the List
            else:
                movie_trailer = {'key': ''}  # Create a Dictionary with an empty Key

            # Set up the Dictionary
            movie_details = {
                "id": full_movie.get('id'),
                "title": full_movie.get('title'),
                "image": full_movie.get('poster_path'),
                "youtube_key": movie_trailer.get('key')
            }

            # Add the Dict to the List of Movies
            movies.append(movie_details)

        # After everything is done, return the List of Movies.
        return movies
