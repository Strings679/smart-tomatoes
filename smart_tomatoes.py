import os
import webbrowser

# <head> of the page. Includes the Meta Tags, CSS and JavaScript.
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Smart Tomatoes - Your premiere movies website</title>
    <!--Import Google Icon Font-->
    <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!--Import materialize.css-->
    <link type="text/css" rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/css/materialize.min.css"
          media="screen,projection"/>

    <!--Let browser know website is optimized for mobile-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <style type="text/css" media="screen">
        body {
            background-color: rgba(250,250,250, 0.84);
        }

        nav {
            margin-bottom: 20px;
            background-color: rgba(10,10,10,0.84);
        }

        #trailer-video {
            width: 100%;
            height: 100%;
        }
    </style>

    <!--Import jQuery before materialize.js-->
    <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <script type="text/javascript"
            src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/js/materialize.min.js"></script>
    <script type="text/javascript" charset="utf-8">
        $(document).ready(function () {
            // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
            $('.modal').modal({
                dismissible: true, // Modal can be dismissed by clicking outside of the modal
                opacity: .5, // Opacity of modal background
                in_duration: 300, // Transition in duration
                out_duration: 200, // Transition out duration
                ready: function (modal, trigger) { // Callback for Modal open.
                    var trailerYouTubeId = trigger.attr('data-trailer-youtube-id');
                    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
                    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
                        'id': 'trailer-video',
                        'type': 'text-html',
                        'src': sourceUrl,
                        'frameborder': 0
                    }));
                },
                complete: function () { // Callback for Modal close
                    $("#trailer-video-container").empty();
                }
            });
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
            $('.card').parent().hide().first().show("fast", function showNext() {
                $(this).next("div").show("fast", showNext);
            });
        });
    </script>
</head>
'''

# The <body> of the page. Includes the NavBar, Modal and Container for the Movies.
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
<body>
<!-- Trailer Video Modal -->
<div id="trailer" class="modal">
    <div class="scale-media" id="trailer-video-container">
    </div>
</div>

<!-- NavBar -->
<nav>
    <div class="container">
        <div class="nav-wrapper">
            <a href="#" class="brand-logo">Smart Tomatoes</a>
        </div>
    </div>
</nav>
    <div class="container">
        <div class="row">
          {movie_tiles}
        </div>
    </div>
  </body>
</html>
'''

# The Content of a Movie. Made to be Iterated and generate a Movie Card.
movie_tile_content = '''
<div class="col s12 m6 l4">
    <div class="card">
        <div class="card-image movie-tile waves-effect waves-block waves-light" data-trailer-youtube-id="{trailer_youtube_id}" data-target="trailer" data-toggle="modal">
            <img src="https://image.tmdb.org/t/p/w500/{poster_image_url}">
        </div>
        <div class="card-content">
            <span class="card-title grey-text text-darken-4">{movie_title}</span>
        </div>
    </div>
</div>
'''


# Procedure to generate the Movie Cards.
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the Card of the Movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.get('title'),
            poster_image_url=movie.get('image'),
            trailer_youtube_id=movie.get('youtube_key')
        )
    return content


# Procedure to Generate a Web Page
def open_movies_page(movies):
    # Create or overwrite the Output file
    output_file = open('index.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # Open the output file in the browser
    url = os.path.abspath(output_file.name)
    print('Done, opening page now.')  # Just for Semantics, to finish the Progress Counter of the API.
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
