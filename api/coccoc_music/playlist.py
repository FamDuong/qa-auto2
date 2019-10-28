import requests

from config.environment import API_COCCOC_PLAYLIST_URL
from config.path import API_COCCOC_MUSIC_LISTING


class Playlist:

    def get_all_playlist(self):
        return requests.get(API_COCCOC_PLAYLIST_URL + API_COCCOC_MUSIC_LISTING,
                            headers={'Content-Type': 'application/json'})





