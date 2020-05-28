import requests

from config.environment import COCCOC_GAME_API_DOMAIN_URL
from config.path import COCCOC_GAME_PUBLIC_EVENTS_ALL_GAMES


class PublicEventsAPI:

    def get_public_events(self):
        return requests.get(COCCOC_GAME_API_DOMAIN_URL + '/v3' + COCCOC_GAME_PUBLIC_EVENTS_ALL_GAMES,
                            headers={'Content-Type': 'application/json'}, )



