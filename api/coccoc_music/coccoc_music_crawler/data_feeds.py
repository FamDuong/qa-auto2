import requests


class DataFeedsAPI(object):

    def show_list_of_data_feeds(self, source_id):
        from config.path import COCCOC_MUSIC_DATA_API
        from config.environment import COCCOC_MUSIC_DATA_DOMAIN_URL
        from config.path import COCCOC_MUSIC_DATA_API_VERSION
        from config.path import COCCOC_MUSIC_DATA_API_VERSION_DATA_FEEDS
        from config.environment import COCCOC_MUSIC_DATA_REGULAR_USER
        from config.environment import COCCOC_MUSIC_DATA_REGULAR_PASSWORD
        return requests.get(COCCOC_MUSIC_DATA_DOMAIN_URL + COCCOC_MUSIC_DATA_API + COCCOC_MUSIC_DATA_API_VERSION
                            + COCCOC_MUSIC_DATA_API_VERSION_DATA_FEEDS,
                            headers={'Content-Type': 'application/json'},
                            auth=(COCCOC_MUSIC_DATA_REGULAR_USER, COCCOC_MUSIC_DATA_REGULAR_PASSWORD),
                            params={'source_id': source_id})















