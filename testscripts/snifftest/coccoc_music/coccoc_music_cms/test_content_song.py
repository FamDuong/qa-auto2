from models.pageobject.coccoc_music.coccoc_music_cms.dash_board_page import CMSDashBoardPageObjects


class TestListSong:
    cms_dash_board = CMSDashBoardPageObjects()

    def test_search_by_song_id(self, browser, set_up_login_then_log_out_after_finish):
        self.cms_dash_board.mouse_over_music_icon(browser)

