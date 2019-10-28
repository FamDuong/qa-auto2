from pytest_testrail.plugin import pytestrail
from api.coccoc_music.playlist import Playlist
from models.api.coccoc_music import playlist as playlist_model


class TestGetPlaylist:

    playlist_api = Playlist()
    playlist_model_instance = playlist_model.Playlist()

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
    def test_validate_field_playlist_item(self):
        list_playlists_response = self.playlist_api.get_all_playlist()
        list_playlists = list_playlists_response.json()
        for playlist in list_playlists:
            assert playlist['type'] in ['1', '2']
        # print(f"List_playlist are : {list_playlists}")
        # print(f"json picke decode are : {jsonpickle_decode}")









