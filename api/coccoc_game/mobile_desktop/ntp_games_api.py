import requests

from config.environment import COCCOC_GAME_API_DOMAIN_URL
from config.path import COCCOC_GAME_NTP_GAMES


class NtpGamesAPI:

    def get_ntp_games_response(self):
        return requests.get(COCCOC_GAME_API_DOMAIN_URL + '/v3' + COCCOC_GAME_NTP_GAMES,
                            headers={'Content-Type': 'application/json'}, )






