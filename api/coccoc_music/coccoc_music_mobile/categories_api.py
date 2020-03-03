import base64

import requests

from config.environment import COCCOC_MUSIC_API_DOMAIN_URL, COCCOC_MUSIC_API_USERNAME, COCCOC_MUSIC_API_PASSWORD
from config.path import COCCOC_MUSIC_API_VERSION, COCCOC_MUSIC_API_CATEGORIES


class CategoriesAPI:

    def get_categories(self):
        return requests.get(COCCOC_MUSIC_API_DOMAIN_URL + COCCOC_MUSIC_API_VERSION + COCCOC_MUSIC_API_CATEGORIES,
                            auth=(COCCOC_MUSIC_API_USERNAME, COCCOC_MUSIC_API_PASSWORD))


