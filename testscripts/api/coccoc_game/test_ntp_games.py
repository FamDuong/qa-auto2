from api.coccoc_game.mobile_desktop.ntp_games_api import NtpGamesAPI
from databases.sql.coccoc_game_api_db import CocCocGameApiDb
from models.api.coccoc_game.ntp_games_schema import NtpGamesSchema
from testscripts.api.coccoc_game.common import check_game_url_format_for_game

game_api_db = CocCocGameApiDb()
ntp_games_api = NtpGamesAPI()


class TestHighlightedGamesNtpGames:

    def test_number_of_highlighted_ntp_games(self, coccoc_game_api_db,):
        ntp_games_api_len = len(ntp_games_api.get_ntp_games_response().json()['results']['highlighted'])
        game_highlighted_db_len = len(game_api_db.get_games_hightlighted_ntp_games_db(connection=coccoc_game_api_db))
        assert ntp_games_api_len == game_highlighted_db_len, "Verify number of hightlighted games in ntp games api match with database"
        assert ntp_games_api_len <= 5, "Verify number of hightlighted games below or equal 5"


class TestRecommendedGamesNtpGames:

    def test_number_of_recommended_ntp_games(self, coccoc_game_api_db,):
        response_json = ntp_games_api.get_ntp_games_response().json()
        ntp_games_highlighted_api_len = len(response_json['results']['highlighted'])
        ntp_games_recommended_api_len = len(response_json['results']['recommended'])
        assert 10 == ntp_games_highlighted_api_len + ntp_games_recommended_api_len, "Total number of highlighted and recommended games is 10"


class TestFormatNtpGames:

    def test_json_object_model_format(self,):
        ntp_games_schema = NtpGamesSchema()
        response_json = ntp_games_api.get_ntp_games_response().json()
        ntp_games_schema.load(response_json)

    def test_game_url_format(self,):
        response_json = ntp_games_api.get_ntp_games_response().json()
        highlighted_games = response_json['results']['highlighted']
        recommended_games = response_json['results']['recommended']
        for each_game in highlighted_games:
            iframe = each_game['iframe']
            game_url = each_game['game_url']
            assert check_game_url_format_for_game(iframe=iframe, game_url=game_url)

        for each_game in recommended_games:
            iframe = each_game['iframe']
            game_url = each_game['game_url']
            assert check_game_url_format_for_game(iframe=iframe, game_url=game_url)



