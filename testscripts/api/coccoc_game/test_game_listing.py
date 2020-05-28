from api.coccoc_game.mobile_desktop.game_listing_api import GameListingAPI
from databases.sql.coccoc_game_api_db import CocCocGameApiDb

game_listing_api = GameListingAPI()
game_api_db = CocCocGameApiDb()


class TestGameListingNumber:

    def test_number_of_games_filter_by_for_mobile(self, coccoc_game_api_db, ):
        number_of_games_from_api = game_listing_api.get_game_listing_data(for_mobile=1).json()['total']
        number_of_games_from_db = len(game_api_db.get_games_by_condition(connection=coccoc_game_api_db, condition="for_mobile = 1"))
        assert number_of_games_from_api == number_of_games_from_db

    def test_number_of_games_filter_by_for_desktop(self, coccoc_game_api_db):
        number_of_games_from_api = game_listing_api.get_game_listing_data(for_desktop=1).json()['total']
        number_of_games_from_db = len(
            game_api_db.get_games_by_condition(connection=coccoc_game_api_db, condition="for_desktop = 1"))
        assert number_of_games_from_api == number_of_games_from_db

    def test_number_of_games_filter_by_hot_game(self, coccoc_game_api_db):
        number_of_games_from_api = game_listing_api.get_game_listing_data(hot_game=1).json()['total']
        number_of_games_from_db = len(
            game_api_db.get_games_by_condition(connection=coccoc_game_api_db, condition="hot_game = 1"))
        assert number_of_games_from_api == number_of_games_from_db

    def test_number_of_games_filter_by_feature_game(self, coccoc_game_api_db):
        number_of_games_from_api = game_listing_api.get_game_listing_data(feature_game=1).json()['total']
        number_of_games_from_db = len(
            game_api_db.get_games_by_condition(connection=coccoc_game_api_db, condition="feature_game = 1"))
        assert number_of_games_from_api == number_of_games_from_db


class TestGameListingSearch:

    def test_search_by_search_term(self):
        pass

    def test_search_by_list_category_id(self):
        pass

    def test_search_by_list_game_id(self):
        pass


class TestGameListingFormat:

    def test_game_listing_format(self):
        pass
