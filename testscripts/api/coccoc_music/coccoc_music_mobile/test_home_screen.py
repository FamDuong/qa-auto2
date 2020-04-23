from pytest_testrail.plugin import pytestrail

from api.coccoc_music.coccoc_music_mobile.home_screen_api import HomeScreenAPI


home_screen_api = HomeScreenAPI()


class TestResults:

    @pytestrail.case('C137256')
    def test_results_object(self):
        pass


class TestPlaylists:

    def test_playlists_object(self):
        print(home_screen_api.get_home_screen_content())






