from example_routes import apply_example_routes
import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /albums
# Returns nothing
#


@app.route('/albums', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    repository.create(Album(None, title, release_year, artist_id))
    return 'Album Created'

# POST /albums
# Returns nothing
# Try it:
#   ; curl http://localhost:5000/albums


@app.route('/albums', methods=['GET'])
def get_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    titles = [album.title for album in albums]
    return ', '.join(titles)


@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    artist_names = [artist.name for artist in artists]
    return ', '.join(artist_names)


@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    repository.create(Artist(None, name, genre))
    return ''


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
