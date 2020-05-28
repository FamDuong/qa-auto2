from api.coccoc_game.mobile_desktop.public_events_api import PublicEventsAPI
from databases.sql.coccoc_game_api_db import CocCocGameApiDb
from testscripts.api.coccoc_game.common import check_game_url_format_for_event

public_events_api = PublicEventsAPI()
game_api_db = CocCocGameApiDb()


class TestListPublicEventsNumber:

    def test_list_public_events_number(self, coccoc_game_api_db, ):
        len_public_events_games = public_events_api.get_public_events().json()['total']
        len_events_db = len(game_api_db.get_game_events_public_events_all_games_db(connection=coccoc_game_api_db))
        assert len_public_events_games == len_events_db, "Verify the number of games matched"


class TestListPublicEventsGameURL:

    def test_game_url_public_events(self, coccoc_game_api_db, ):
        response_json = public_events_api.get_public_events().json()
        results_events_list = response_json['results']
        for each_event in results_events_list[0:4]:
            game_id = each_event['game_id']
            iframe = game_api_db.get_iframe_by_game_id(coccoc_game_api_db, game_id=game_id)[0]
            game_url = each_event['game_url']
            assert check_game_url_format_for_event(iframe=iframe, game_url_for_event=game_url)


