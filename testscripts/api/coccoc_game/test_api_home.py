from api.coccoc_game.mobile_desktop.home_screen_api import GameHomeScreenAPI
from databases.sql.coccoc_game_api_db import CocCocGameApiDb
from models.api.coccoc_game.home_game_schema import HomeGameSchema

game_home_screen_api = GameHomeScreenAPI()
game_api_db = CocCocGameApiDb()


class TestHighlightGamesHome:

    def test_number_of_highlighted_games(self, coccoc_game_api_db):
        api_game_highlighted_len = len(game_home_screen_api.get_home_screen_content().json()['results']['highlighted'])
        game_highlighted_db_len = len(game_api_db.get_games_hightlighted_home_api_db(coccoc_game_api_db))
        assert api_game_highlighted_len == game_highlighted_db_len, "Verify number of hightlighted games in home_screen api match with database"
        assert api_game_highlighted_len <= 20, "Verify number of hightlighted games below or equal 20"


class TestGameCategoriesHome:

    def test_number_of_game_category(self, coccoc_game_api_db):
        api_game_categories_len = 0
        for each_category in game_home_screen_api.get_home_screen_content().json()['results']['game_category']:
            api_game_categories_len += len(each_category['games'])
        game_categories_db_len = len(game_api_db.get_games_categories_db(coccoc_game_api_db))
        assert api_game_categories_len == game_categories_db_len, "Verify number of hightlighted games in home_screen api match with database"


class TestRecommendedGamesHome:

    def test_number_of_recommended_games(self, coccoc_game_api_db):
        excluded_game_ids = []
        for each_game_id in game_api_db.get_game_ids_for_hightlighted_home_api_db(coccoc_game_api_db):
            excluded_game_ids.append(each_game_id[0])
        recommended_game_from_db_len = len(game_api_db.get_game_recommended_home_api_db(coccoc_game_api_db, exclude_game_id=tuple(excluded_game_ids)))
        api_game_recommended_len = len(game_home_screen_api.get_home_screen_content().json()['results']['recommended'])
        assert recommended_game_from_db_len == api_game_recommended_len, "Verify number of recommended games matched to db"

import requests

class TestFormatResponseHome:

    def test_response_home_game(self,):
        home_game_schema = HomeGameSchema()
        response_json = game_home_screen_api.get_home_screen_content().json()
        home_game_schema.load(response_json)


    def test_api(self):
        dev_api_url = 'https://dev-browser-game-api.coccoc.com/api/v3/public-events-all-games'
        prd_api_url = 'https://browser-game-api.coccoc.com/api/v3/public-events-all-games'
        with requests.Session() as session:
            initial_response = session.get(dev_api_url)
            response = session.get(dev_api_url)

        print(response.text)



