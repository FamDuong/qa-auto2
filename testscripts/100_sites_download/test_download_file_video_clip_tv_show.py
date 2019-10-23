from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail

from testscripts.common_setup import download_file_via_main_download_button, \
    assert_file_download_value, delete_all_mp4_file_download
from utils_automation.const import OtherSiteUrls

savior_page_object = SaviorPageObject()
any_site_page_object = AnySitePageObject()


class TestDailyMotion:

    @staticmethod
    def mouse_over_video_for_displaying_savior(browser):
        browser.get(OtherSiteUrls.DAILY_MOTION_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_daily_motion(browser)

    @pytestrail.case('C98793')
    def test_download_file_daily_motion(self, browser, get_current_download_folder):
        self.mouse_over_video_for_displaying_savior(browser)
        try:
            download_file_via_main_download_button(browser)
            self.mouse_over_video_for_displaying_savior(browser)
            savior_page_object.choose_preferred_option(browser)
            height_frame = savior_page_object.verify_correct_video_options_chosen_high_quality_option(browser)
            # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)
        finally:
            delete_all_mp4_file_download(get_current_download_folder, '.mp4')


class TestVliveTV:

    @staticmethod
    def mouse_over_video_for_displaying_savior(browser):
        browser.get(OtherSiteUrls.VLIVE_TV_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_vlive_tv(browser)

    @pytestrail.case('C98809')
    def test_download_file_vlive_tv(self, browser, get_current_download_folder):
        self.mouse_over_video_for_displaying_savior(browser)
        try:
            download_file_via_main_download_button(browser)
            self.mouse_over_video_for_displaying_savior(browser)
            savior_page_object.choose_preferred_option(browser)
            height_frame = savior_page_object.verify_correct_video_options_chosen_high_quality_option(browser)
            # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)
        finally:
            delete_all_mp4_file_download(get_current_download_folder, '.mp4')




