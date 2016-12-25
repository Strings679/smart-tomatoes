# Smart Tomatoes

This is a simple project made with **Python** for the _Movie Trailer Website_ project.
It contains Python Scripts to generate the html file of a Website, that contains movies
obtained from [The Movie DB](https://www.themoviedb.org/) through their API. 

## Setup

1. Clone this repository: `git clone https://github.com/mikelfcosta/smart-tomatoes`
2. Get an API key from The Movie DB: https://developers.themoviedb.org/3/getting-started
3. Insert your API Key on the `api.py` file.
4. If you don't have it, install requests using PIP: `pip install requests`

## Usage

In order to generate the HTML file, you need to run the `media.py` file. Inside it, you can change the Genre ID to
generate the website with movies from a different genre. 

This project uses the `/discover/movies` API, and from the `GetMovie` class
you can call the method `search_by_genre`, passing the genre ID as a parameter to get the movies from this genre.

These genre IDs come from The Movie DB API,
and [you can click here to learn more about they](https://developers.themoviedb.org/3/genres).

### Dependencies

This project requires the following dependencies:

- [Requests](https://github.com/kennethreitz/requests): Requests allows you to send organic, grass-fed HTTP/1.1
requests, without the need for manual labor. Used to make HTTP requests to The Movie DB API.
- [Materialize](https://github.com/Dogfalo/materialize): A CSS Framework based on material design

### Known Issues

- Depending on the aspect-ratio of the imported images, the column layout may break and jump one row. A solution to
this is a work in progress, feel free to submit a fix if you find it.

## License

>You can check out the full license [here](https://github.com/mikelfcosta/fresh-tomatoes/blob/master/LICENSE.md)

This project is licensed under the terms of the **MIT** license.