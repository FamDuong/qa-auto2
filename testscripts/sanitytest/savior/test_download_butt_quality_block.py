import pytest
from models.pageobject.downloads import DownloadsPageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.settings import SettingsPageObject
from models.pageobject.sites import YoutubePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.common_setup import revert_high_quality_default_option, pause_any_video_site, \
    choose_video_quality_medium_option, \
    choose_video_quality_low_option, delete_all_mp4_file_download, download_file_via_main_download_button, \
    check_if_the_file_fully_downloaded, assert_file_download_value, clear_data_download, get_resolution_info
from utils_automation.const import VideoUrls, DiffFormatFileUrls
from utils_automation.setup import WaitAfterEach


class TestDownloadButtQualityBlock:
    youtube_page_object = YoutubePageObject()
    savior_page_object = SaviorPageObject()
    setting_page_obeject = SettingsPageObject()

    download_page_object = DownloadsPageObject()

    def prepare_check_download(self, browser, download_folder):
        delete_all_mp4_file_download(download_folder, '.mp4')
        self.prepare_youtube_savior(browser)
        WaitAfterEach.sleep_timer_after_each_step()

    def download_file_medium(self, browser):
        self.savior_page_object.download_file_medium_quality(browser)
        WaitAfterEach.sleep_timer_after_each_step()

        check_if_the_file_fully_downloaded(browser)

    def download_file_high(self, browser):
        self.savior_page_object.download_file_high_quality(browser)
        WaitAfterEach.sleep_timer_after_each_step()

        check_if_the_file_fully_downloaded(browser)

    def download_file_low(self, browser):
        self.savior_page_object.download_file_low_quality(browser)
        WaitAfterEach.sleep_timer_after_each_step()

        check_if_the_file_fully_downloaded(browser)

    def prepare_youtube_savior(self, browser):
        youtube_page_object = YoutubePageObject()
        browser.get(VideoUrls.YOUTUBE_VIDEO_URL)
        youtube_page_object.mouse_over_video_item(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.prepare_youtube_savior(browser)
        self.savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_check_click_download_button_default_quality(self, browser, get_current_download_folder):
        self.prepare_check_download(browser, get_current_download_folder)
        try:
            media_info = download_file_via_main_download_button(browser)
            height_frame = get_resolution_info(media_info)
            # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)
        finally:
            clear_data_download(browser)

    @pytestrail.case('C54153')
    @pytest.mark.parametrize('url_site', [i for i in DiffFormatFileUrls.all()])
    @pytest.mark.skip(reason='This test should be implemented in API or UI level')
    def test_check_download_different_format(self, browser, url_site, get_current_download_folder):
        self.prepare_check_download(browser, get_current_download_folder)

        self.savior_page_object.choose_preferred_option(browser)

        try:
            # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, 360)
        finally:
            clear_data_download(browser)
            revert_high_quality_default_option(browser)

    @pytestrail.case('C54154')
    @pytest.mark.skip(reason='Duplicated test with C54152')
    def test_check_when_preferred_quality_high(self, browser, get_current_download_folder):
        revert_high_quality_default_option(browser)
        self.prepare_check_download(browser, get_current_download_folder)
        try:
            media_info = download_file_via_main_download_button(browser)
            height_frame = get_resolution_info(media_info)
        # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)
        finally:
            clear_data_download(browser)

    @pytestrail.case('C54155')
    def test_check_when_preferred_quality_medium(self, browser, get_current_download_folder):
        choose_video_quality_medium_option(browser)
        self.prepare_check_download(browser, get_current_download_folder)
        try:
            media_info = download_file_via_main_download_button(browser)
            height_frame = get_resolution_info(media_info)
            # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)

        finally:
            clear_data_download(browser)
            revert_high_quality_default_option(browser)

    @pytestrail.case('C54156')
    def test_check_when_preferred_quality_low(self, browser, get_current_download_folder):
        choose_video_quality_low_option(browser)
        self.prepare_check_download(browser, get_current_download_folder)
        try:
            media_info = download_file_via_main_download_button(browser)
            height_frame = get_resolution_info(media_info)
            # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)

        finally:
            clear_data_download(browser)
            revert_high_quality_default_option(browser)
