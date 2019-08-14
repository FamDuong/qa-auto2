import time

import cv2

from models.pageobject.downloads import DownloadsPageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.settings import SettingsPageObject
from models.pageobject.sites import YoutubePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import pause_any_video_youtube, get_text_extension_option, \
    savior_extension, revert_high_quality_default_option
from utils_automation.cleanup import Files
from utils_automation.common import FilesHandle
from utils_automation.const import Urls


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
        time.sleep(2)
        self.download_page_object.clear_all_existed_downloads(driver)
        time.sleep(2)

    def check_if_the_file_fully_downloaded(self, browser):
        browser.get(Urls.COCCOC_DOWNLOAD_URL)
        self.download_page_object.verify_play_button_existed(browser)

    def prepare_check_download(self, browser):
        browser.get(Urls.COCCOC_SETTINGS_URL)
        download_folder_path = self.setting_page_obeject.get_download_folder(browser)
        self.delete_all_mp4_file_download(download_folder_path, '.mp4')

        pause_any_video_youtube(browser)
        time.sleep(2)
        return download_folder_path

    def download_file_default(self, browser):
        self.savior_page_object.download_file_via_savior_download_btn(browser)
        time.sleep(3)

        # Check the file is fully downloaded
        self.check_if_the_file_fully_downloaded(browser)

    def download_file_medium(self, browser):
        self.savior_page_object.download_file_medium_quality(browser)
        time.sleep(3)

        self.check_if_the_file_fully_downloaded(browser)

    def download_file_high(self, browser):
        self.savior_page_object.download_file_high_quality(browser)
        time.sleep(3)

        self.check_if_the_file_fully_downloaded(browser)

    def download_file_low(self, browser):
        self.savior_page_object.download_file_low_quality(browser)
        time.sleep(3)

        self.check_if_the_file_fully_downloaded(browser)

    def assert_file_download_value(self,download_folder_path, height_value, width_value):
        mp4_files = self.find_mp4_file_download(download_folder_path, '.mp4')
        print(mp4_files)
        vid = cv2.VideoCapture(download_folder_path + '\\' + mp4_files[0])
        height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        assert height == height_value
        assert width == width_value

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        pause_any_video_youtube(browser)
        self.savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_check_click_download_button(self, browser):
        # time.sleep(2)
        # Deletes all mp4 files and pause any video youtube
        download_folder_path = self.prepare_check_download(browser)
        try:
            self.download_file_default(browser)
        # File mp4 file and assert
            self.assert_file_download_value(download_folder_path, 720, 1280)
        finally:
            self.clear_data_download(browser)

    @pytestrail.case('C54153')
    def test_check_download_different_format(self, browser):
        download_folder_path = self.prepare_check_download(browser)

        self.savior_page_object.choose_preferred_option(browser)

        self.savior_page_object.choose_medium_option(browser)

        try:
            self.download_file_medium(browser)
        # File mp4 file and assert
            self.assert_file_download_value(download_folder_path, 360, 640)
        finally:
            self.clear_data_download(browser)
            revert_high_quality_default_option(browser)

    @pytestrail.case('C54154')
    def test_check_when_preferred_quality_high(self, browser):
        download_folder_path = self.prepare_check_download(browser)
        self.savior_page_object.choose_preferred_option(browser)

        self.savior_page_object.choose_high_option(browser)
        try:
            self.download_file_high(browser)
        # File mp4 file and assert
            self.assert_file_download_value(download_folder_path, 720, 1280)
        finally:
            self.clear_data_download(browser)

    @pytestrail.case('C54155')
    def test_check_when_preferred_quality_medium(self, browser):
        download_folder_path = self.prepare_check_download(browser)
        self.savior_page_object.choose_preferred_option(browser)

        self.savior_page_object.choose_medium_option(browser)
        try:
            self.download_file_medium(browser)
            # File mp4 file and assert
            self.assert_file_download_value(download_folder_path, 360, 640)
        finally:
            self.clear_data_download(browser)
            revert_high_quality_default_option(browser)

    @pytestrail.case('C54156')
    def test_check_when_preferred_quality_low(self, browser):
        download_folder_path = self.prepare_check_download(browser)
        self.savior_page_object.choose_preferred_option(browser)

        self.savior_page_object.choose_low_option(browser)
        try:
            self.download_file_low(browser)
            # File mp4 file and assert
            self.assert_file_download_value(download_folder_path, 240, 426)
        finally:
            self.clear_data_download(browser)
            revert_high_quality_default_option(browser)
