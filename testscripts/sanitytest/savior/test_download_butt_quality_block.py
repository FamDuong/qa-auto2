import time

import cv2
import pytest


from models.pageobject.downloads import DownloadsPageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.settings import SettingsPageObject
from models.pageobject.sites import YoutubePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import pause_any_video_youtube, get_text_extension_option, \
    savior_extension, revert_high_quality_default_option, pause_any_video_site, choose_video_quality_medium_option, \
    choose_video_quality_low_option
from utils_automation.cleanup import Files
from utils_automation.common import FilesHandle
from utils_automation.const import Urls, VideoUrls, DiffFormatFileUrls
from utils_automation.setup import WaitAfterEach


class TestDownloadButtQualityBlock:
    youtube_page_object = YoutubePageObject()
    savior_page_object = SaviorPageObject()
    setting_page_obeject = SettingsPageObject()

    download_page_object = DownloadsPageObject()

    def delete_all_mp4_file_download(self, mydir, endwith):
        files = Files()
        files.delete_files_in_folder(mydir, endwith)

    def find_mp4_file_download(self, mydir, endwith):
        files_handle = FilesHandle()
        return files_handle.find_files_in_folder_by_modified_date(mydir, endwith)

    def clear_data_download(self, driver):
        driver.get(Urls.COCCOC_DOWNLOAD_URL)
        WaitAfterEach.sleep_timer_after_each_step()
        self.download_page_object.clear_all_existed_downloads(driver)
        WaitAfterEach.sleep_timer_after_each_step()

    def check_if_the_file_fully_downloaded(self, browser):
        browser.get(Urls.COCCOC_DOWNLOAD_URL)
        self.download_page_object.verify_play_button_existed(browser)

    def prepare_check_download(self, browser, url_site, download_folder):
        browser.get(Urls.COCCOC_SETTINGS_URL)
        # download_folder_path = self.setting_page_obeject.get_download_folder(browser)
        self.delete_all_mp4_file_download(download_folder, '.mp4')

        pause_any_video_site(browser, url_site)
        WaitAfterEach.sleep_timer_after_each_step()
        # return download_folder_path

    def download_file_via_main_download_button(self, browser):
        self.savior_page_object.download_file_via_savior_download_btn(browser)
        WaitAfterEach.sleep_timer_after_each_step()

        # Check the file is fully downloaded
        self.check_if_the_file_fully_downloaded(browser)

    def download_file_medium(self, browser):
        self.savior_page_object.download_file_medium_quality(browser)
        WaitAfterEach.sleep_timer_after_each_step()

        self.check_if_the_file_fully_downloaded(browser)

    def download_file_high(self, browser):
        self.savior_page_object.download_file_high_quality(browser)
        WaitAfterEach.sleep_timer_after_each_step()

        self.check_if_the_file_fully_downloaded(browser)

    def download_file_low(self, browser):
        self.savior_page_object.download_file_low_quality(browser)
        WaitAfterEach.sleep_timer_after_each_step()

        self.check_if_the_file_fully_downloaded(browser)

    def assert_file_download_value(self, download_folder_path, height_value):
        mp4_files = self.find_mp4_file_download(download_folder_path, '.mp4')
        print(mp4_files)
        vid = cv2.VideoCapture(download_folder_path + '\\' + mp4_files[0])
        height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        vid.release()
        if (height_value is not None) and (height_value != ''):
            assert str(int(height)) in height_value
        else:
            assert height is not None

    @pytestrail.case('C54151')
    @pytest.mark.parametrize('url_site', [i for i in VideoUrls.all()])
    def test_check_default_state_download_button(self, browser, url_site):
        pause_any_video_site(browser, url_site)
        self.savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    @pytest.mark.parametrize('url_site', [i for i in VideoUrls.all()])
    def test_check_click_download_button_default_quality(self, browser, url_site, get_current_download_folder):
        # time.sleep(2)
        # Deletes all mp4 files and pause any video youtube
        self.prepare_check_download(browser, url_site, get_current_download_folder)
        try:
            self.download_file_via_main_download_button(browser)
            pause_any_video_site(browser, url_site)
            self.savior_page_object.choose_preferred_option(browser)
            height_frame = self.savior_page_object.verify_correct_video_options_chosen_high_quality_option(browser)
            # File mp4 file and assert
            self.assert_file_download_value(get_current_download_folder, height_frame)
        finally:
            self.clear_data_download(browser)

    @pytestrail.case('C54153')
    @pytest.mark.parametrize('url_site', [i for i in DiffFormatFileUrls.all()])
    @pytest.mark.skip(reason='Waiting for implemented')
    def test_check_download_different_format(self, browser, url_site, get_current_download_folder):
        self.prepare_check_download(browser, url_site, get_current_download_folder)

        self.savior_page_object.choose_preferred_option(browser)

        try:
            # File mp4 file and assert
            self.assert_file_download_value(get_current_download_folder, 360)
        finally:
            self.clear_data_download(browser)
            revert_high_quality_default_option(browser)

    @pytestrail.case('C54154')
    @pytest.mark.parametrize('url_site', [i for i in VideoUrls.all()])
    @pytest.mark.skip(reason='Duplicated test with C54152')
    def test_check_when_preferred_quality_high(self, browser, url_site, get_current_download_folder):
        revert_high_quality_default_option(browser)
        self.prepare_check_download(browser, url_site, get_current_download_folder)
        try:
            self.download_file_via_main_download_button(browser)
            pause_any_video_site(browser, url_site)
            self.savior_page_object.choose_preferred_option(browser)
            height_frame = self.savior_page_object.verify_correct_video_options_chosen_high_quality_option(browser)

        # File mp4 file and assert
            self.assert_file_download_value(get_current_download_folder, height_frame)
        finally:
            self.clear_data_download(browser)

    @pytestrail.case('C54155')
    @pytest.mark.parametrize('url_site', [i for i in VideoUrls.all()])
    def test_check_when_preferred_quality_medium(self, browser, url_site, get_current_download_folder):
        choose_video_quality_medium_option(browser)
        self.prepare_check_download(browser, url_site, get_current_download_folder)
        try:
            self.download_file_via_main_download_button(browser)
            pause_any_video_site(browser, url_site)
            self.savior_page_object.choose_preferred_option(browser)
            height_frame = self.savior_page_object.verify_correct_video_options_chosen_medium_quality_option(browser)

            # File mp4 file and assert
            self.assert_file_download_value(get_current_download_folder, height_frame)

        finally:
            self.clear_data_download(browser)
            revert_high_quality_default_option(browser)

    @pytestrail.case('C54156')
    @pytest.mark.parametrize('url_site', [i for i in VideoUrls.all()])
    def test_check_when_preferred_quality_low(self, browser, url_site, get_current_download_folder):
        choose_video_quality_low_option(browser)
        self.prepare_check_download(browser, url_site, get_current_download_folder)
        try:
            self.download_file_via_main_download_button(browser)
            pause_any_video_site(browser, url_site)
            self.savior_page_object.choose_preferred_option(browser)
            height_frame = self.savior_page_object.verify_correct_video_options_chosen_low_quality_option(browser)

            # File mp4 file and assert
            self.assert_file_download_value(get_current_download_folder, height_frame)

        finally:
            self.clear_data_download(browser)
            revert_high_quality_default_option(browser)
