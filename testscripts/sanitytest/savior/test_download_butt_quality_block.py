import time

import cv2
import pytest


from models.pageobject.downloads import DownloadsPageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.settings import SettingsPageObject
from models.pageobject.sites import YoutubePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import revert_high_quality_default_option, pause_any_video_site, \
    choose_video_quality_medium_option, \
    choose_video_quality_low_option, delete_all_mp4_file_download, download_file_via_main_download_button, \
    check_if_the_file_fully_downloaded, assert_file_download_value, clear_data_download
from utils_automation.const import Urls, VideoUrls, DiffFormatFileUrls
from utils_automation.setup import WaitAfterEach


class TestDownloadButtQualityBlock:
    youtube_page_object = YoutubePageObject()
    savior_page_object = SaviorPageObject()
    setting_page_obeject = SettingsPageObject()

    download_page_object = DownloadsPageObject()

    def prepare_check_download(self, browser, url_site, download_folder):
        browser.get(Urls.COCCOC_SETTINGS_URL)
        # download_folder_path = self.setting_page_obeject.get_download_folder(browser)
        delete_all_mp4_file_download(download_folder, '.mp4')

        pause_any_video_site(browser, url_site)
        WaitAfterEach.sleep_timer_after_each_step()
        # return download_folder_path

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

    @pytestrail.case('C54151')
    @pytest.mark.parametrize('url_site', [i for i in VideoUrls.all()])
    def test_check_default_state_download_button(self, browser, url_site):
        pause_any_video_site(browser, url_site)
        self.savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    @pytest.mark.parametrize('url_site', [i for i in VideoUrls.all()])
    def test_check_click_download_button_default_quality(self, browser, url_site, get_current_download_folder):
        self.prepare_check_download(browser, url_site, get_current_download_folder)
        try:
            if url_site in [VideoUrls.BILU_TV_VIDEO_URL, VideoUrls.DONG_PHIM_VIDEO_URL]:
                download_file_via_main_download_button(browser, file_type='movie')
            else:
                download_file_via_main_download_button(browser)
            pause_any_video_site(browser, url_site)
            self.savior_page_object.choose_preferred_option(browser)
            height_frame = self.savior_page_object.verify_correct_video_options_chosen_high_quality_option(browser)
            # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)
        finally:
            clear_data_download(browser)

    @pytestrail.case('C54153')
    @pytest.mark.parametrize('url_site', [i for i in DiffFormatFileUrls.all()])
    @pytest.mark.skip(reason='Waiting for implemented')
    def test_check_download_different_format(self, browser, url_site, get_current_download_folder):
        self.prepare_check_download(browser, url_site, get_current_download_folder)

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
        self.prepare_check_download(browser, VideoUrls.YOUTUBE_VIDEO_URL, get_current_download_folder)
        try:
            download_file_via_main_download_button(browser)
            pause_any_video_site(browser, VideoUrls.YOUTUBE_VIDEO_URL)
            self.savior_page_object.choose_preferred_option(browser)
            height_frame = self.savior_page_object.verify_correct_video_options_chosen_high_quality_option(browser)

        # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)
        finally:
            clear_data_download(browser)

    @pytestrail.case('C54155')
    def test_check_when_preferred_quality_medium(self, browser, get_current_download_folder):
        choose_video_quality_medium_option(browser)
        self.prepare_check_download(browser, VideoUrls.YOUTUBE_VIDEO_URL, get_current_download_folder)
        try:
            download_file_via_main_download_button(browser)
            pause_any_video_site(browser, VideoUrls.YOUTUBE_VIDEO_URL)
            self.savior_page_object.choose_preferred_option(browser)
            height_frame = self.savior_page_object.verify_correct_video_options_chosen_medium_quality_option(browser)

            # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)

        finally:
            clear_data_download(browser)
            revert_high_quality_default_option(browser)

    @pytestrail.case('C54156')
    def test_check_when_preferred_quality_low(self, browser, get_current_download_folder):
        choose_video_quality_low_option(browser)
        self.prepare_check_download(browser, VideoUrls.YOUTUBE_VIDEO_URL, get_current_download_folder)
        try:
            download_file_via_main_download_button(browser)
            pause_any_video_site(browser, VideoUrls.YOUTUBE_VIDEO_URL)
            self.savior_page_object.choose_preferred_option(browser)
            height_frame = self.savior_page_object.verify_correct_video_options_chosen_low_quality_option(browser)

            # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)

        finally:
            clear_data_download(browser)
            revert_high_quality_default_option(browser)
