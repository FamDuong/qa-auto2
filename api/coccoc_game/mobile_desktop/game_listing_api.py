import requests

from config.environment import COCCOC_GAME_API_DOMAIN_URL
from config.path import COCCOC_GAME_GAMES


class GameListingAPI:

    def get_game_listing_data(self, for_mobile=0, for_desktop=0, hot_game=0, feature_game=0, search_term=None,
                              list_category_id=None, list_game_id=None, order_by=None, per_page=0, page=0):
        params = dict()
        if for_mobile:
            params['for_mobile'] = for_mobile
        if for_desktop:
            params['for_desktop'] = for_desktop
        if hot_game:
            params['hot_game'] = hot_game
        if feature_game:
            params['feature_game'] = feature_game
        if search_term:
            params['search_term'] = search_term
        if list_category_id:
            params['list_category_id'] = list_category_id
        if list_game_id:
            params['list_game_id'] = list_game_id
        if order_by:
            params['order_by'] = order_by
        if per_page:
            params['per_page'] = per_page
        if page:
            params['page'] = page
        return requests.get(COCCOC_GAME_API_DOMAIN_URL + '/v2' + COCCOC_GAME_GAMES,
                            headers={'Content-Type': 'application/json'},
                            params=params)




