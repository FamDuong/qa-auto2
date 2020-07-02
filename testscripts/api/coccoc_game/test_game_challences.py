from api.coccoc_game.mobile_desktop.game_challences import MobileGameApi

class TestGameChallences:
    game_api = MobileGameApi()

    def test_game_challence(self):
        self.game_api.request()
