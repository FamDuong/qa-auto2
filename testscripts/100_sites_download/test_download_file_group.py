import pytest
from models.pageobject.savior import SaviorPageObject
from pytest_testrail.plugin import pytestrail

from models.pageobject.settings import SettingsPageObject
from models.pageobject.sites import AnySitePageObject
from testscripts.common_setup import pause_any_video_site, download_file_via_main_download_button, \
    assert_file_download_value, delete_all_mp4_file_download, \
    implement_download_file
from utils_automation.const import VideoUrls, Urls
from utils_automation.setup import WaitAfterEach

any_site_page_object = AnySitePageObject()


class TestDownloadGroup:

    savior_page_object = SaviorPageObject()

    @staticmethod
    def prepare_check_download(download_folder):
        delete_all_mp4_file_download(download_folder, '.mp4')
        WaitAfterEach.sleep_timer_after_each_step()

    def implement_test_site(self, browser, url_site, get_current_download_folder):
        pause_any_video_site(browser, url_site)
        self.prepare_check_download(get_current_download_folder)
        download_file_via_main_download_button(browser, )
        pause_any_video_site(browser, url_site)
        self.savior_page_object.choose_preferred_option(browser)
        height_frame = self.savior_page_object.verify_correct_video_options_chosen_high_quality_option(browser)
        # File mp4 file and assert
        assert_file_download_value(get_current_download_folder, height_frame)

    @pytestrail.case('C96719')
    @pytest.mark.ten_popular_sites
    def test_download_youtube(self, browser, get_current_download_folder, clear_download_page_and_download_folder):
        self.implement_test_site(browser, VideoUrls.YOUTUBE_VIDEO_URL, get_current_download_folder)

    @pytestrail.case('C96752')
    def test_download_news_zing(self, browser, get_current_download_folder, clear_download_page_and_download_folder):
        self.implement_test_site(browser, VideoUrls.NEWS_ZING_VIDEO_URL, get_current_download_folder)

    @pytestrail.case('C96756')
    def test_download_zing_mp3_vn(self, browser, get_current_download_folder, clear_download_page_and_download_folder):
        self.implement_test_site(browser, VideoUrls.ZING_MP3_VN_VIDEO_URL, get_current_download_folder)

    @pytestrail.case('C96758')
    @pytest.mark.ten_popular_sites
    def test_download_nhaccuatui(self, browser, get_current_download_folder, clear_download_page_and_download_folder
                                 , disable_coccoc_block_ads):
        self.implement_test_site(browser, VideoUrls.NHAC_CUA_TUI_VIDEO_ITEM, get_current_download_folder)

    @pytestrail.case('C98735')
    @pytest.mark.ten_popular_sites
    def test_download_dongphim(self, browser, get_current_download_folder, clear_download_page_and_download_folder):
        browser.get(VideoUrls.DONG_PHIM_VIDEO_URL)
        WaitAfterEach.sleep_timer_after_each_step()
        any_site_page_object.click_video_item_dong_phim(browser)
        any_site_page_object.choose_watch_option_if_any(browser)
        any_site_page_object.mouse_over_video_item_dong_phim(browser)
        implement_download_file(browser, get_current_download_folder, ),





