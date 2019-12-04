import requests
from pytest_testrail.plugin import pytestrail
from api.coccoc_music.playlist import Playlist
from models.api.coccoc_music import playlist_schema as playlist_model


class TestGetPlaylist:

    playlist_api = Playlist()
    playlist_schema = playlist_model.PlaylistSchema()

    @pytestrail.case('C119381')
    def test_number_of_songs(self):
        list_playlists_response = self.playlist_api.get_all_playlist()
        list_playlists = list_playlists_response.json()
        number_of_songs = 0
        number_of_songs_assert = 5000
        for playlist in list_playlists:
            number_of_songs += len(playlist['items'])
        print(f"Number of songs in the list are : {number_of_songs}")
        assert number_of_songs < number_of_songs_assert, f"Number of songs must be below : {number_of_songs_assert}"

    @pytestrail.case('C119382')
    def test_fields_playlist_song_item(self):
        list_playlists_response = self.playlist_api.get_all_playlist()
        list_playlists = list_playlists_response.json()
        for playlist in list_playlists:
            self.playlist_schema.load(playlist)

    @pytestrail.case('C121607')
    def test_song_url(self):
        list_playlists_response = self.playlist_api.get_all_playlist()
        list_playlists = list_playlists_response.json()
        number_of_songs = 0
        items_url = []
        sample = []
        for playlist in list_playlists:
            number_of_songs += len(playlist['items'])
            import random
            sample = random.sample(range(0, number_of_songs - 1), 10)
            for item in playlist['items']:
                items_url.append(item['url'])
        for item in sample:
            response = requests.get(items_url[item])
            assert response.status_code == 200
            assert 'flashPlayer' in str(response.content)







