# Tests for your routes go here

# === Example Code Below ===

"""
POST /albums
Body Params:
    title=Voyage
    release_year=2022
    artist_id=2
Returns:
    Nothing
Side effects:
    Adds album to db
"""


def test_post_album(db_connection, web_client):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.post(
        "/albums", data={'title': 'Test Album', 'release_year': 2000, 'artist_id': 1})
    assert response.status_code == 200
    assert web_client.get("/albums").data.decode(
        'utf-8') == 'Group Therapy, Whats The Story Morning Glory, Test Album'


def test_get_albums(db_connection, web_client):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode(
        'utf-8') == 'Group Therapy, Whats The Story Morning Glory'


'''
Get /artists
Returns list of artists in a string
Response Status 200
e.g. Taylor Swift, Above and Beyond
'''


def test_get_artists(db_connection, web_client):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Taylor Swift, Above and Beyond'


def test_post_artist(db_connection, web_client):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.post(
        '/artists', data={'name': 'Wild Nothing', 'genre': 'Indie'})
    artists = web_client.get('/artists')
    assert response.status_code == 200
    assert artists.data.decode(
        'utf-8') == 'Taylor Swift, Above and Beyond, Wild Nothing'


# === End Example Code ===
