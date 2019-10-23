import pytest

from models.pageobject.savior import SaviorPageObject
from pytest_testrail.plugin import pytestrail
from testscripts.common_setup import pause_any_video_youtube


class TestSubTitleDownload:
    savior_page_object = SaviorPageObject()

    @pytestrail.case('C54165')
    def test_check_if_sub_detected_hover_media_player(self, browser):
        pause_any_video_youtube(browser)
        self.savior_page_object.choose_preferred_option(browser)
        self.savior_page_object.verify_all_subtitles_displayed(browser, 'English', 'Japanese', 'Vietnamese')

    @pytestrail.case('C54166')
    @pytest.mark.skip(reason='Will implement with pywinauto later')
    def test_check_if_subtitle_detected_savior_button(self, browser):
        pass

    @pytestrail.case('C54167')
    @pytest.mark.skip(reason='Will implement test after update the test case description')
    def test_check_if_download_subtitle_supported(self, browser):
        pass


