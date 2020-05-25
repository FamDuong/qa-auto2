import requests

from config.environment import COCCOC_GAME_API_DOMAIN_URL
from config.path import COCCOC_GAME_API_HOME


class GameHomeScreenAPI:

    def get_home_screen_content(self):
        return requests.get(COCCOC_GAME_API_DOMAIN_URL + '/v3' + COCCOC_GAME_API_HOME,
                            headers={'Content-Type': 'application/json'},)



