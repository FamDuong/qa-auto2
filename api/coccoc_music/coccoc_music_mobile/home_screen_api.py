import requests
from requests.auth import HTTPBasicAuth

from config.environment import COCCOC_MUSIC_API_DOMAIN_URL, COCCOC_MUSIC_API_USERNAME, COCCOC_MUSIC_API_PASSWORD
from config.path import COCCOC_MUSIC_API_VERSION, COCCOC_MUSIC_API_HOME


class HomeScreenAPI:

    def get_home_screen_content(self):
        return requests.get(COCCOC_MUSIC_API_DOMAIN_URL + COCCOC_MUSIC_API_VERSION + COCCOC_MUSIC_API_HOME,
                            auth=HTTPBasicAuth(COCCOC_MUSIC_API_USERNAME, COCCOC_MUSIC_API_PASSWORD),
                            headers={'Content-Type': 'application/json'},)




