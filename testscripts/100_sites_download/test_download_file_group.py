from models.pageobject.savior import SaviorPageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import pause_any_video_site, download_file_via_main_download_button, \
    assert_file_download_value, clear_data_download, delete_all_mp4_file_download
from utils_automation.const import VideoUrls
from utils_automation.setup import WaitAfterEach


class TestDownloadGroup:

    savior_page_object = SaviorPageObject()

    @staticmethod
    def prepare_check_download(browser, url_site, download_folder):
        delete_all_mp4_file_download(download_folder, '.mp4')
        pause_any_video_site(browser, url_site)
        WaitAfterEach.sleep_timer_after_each_step()

    def implement_test_site(self, browser, url_site, get_current_download_folder):
        pause_any_video_site(browser, url_site)
        self.savior_page_object.assert_value_preferred_quality(browser, 'High')
        self.prepare_check_download(browser, url_site, get_current_download_folder)
        try:
            if url_site is VideoUrls.DONG_PHIM_VIDEO_URL:
                download_file_via_main_download_button(browser, file_type='slow')
            else:
                download_file_via_main_download_button(browser)
            pause_any_video_site(browser, url_site)
            self.savior_page_object.choose_preferred_option(browser)
            height_frame = self.savior_page_object.verify_correct_video_options_chosen_high_quality_option(browser)
            # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)
        finally:
            clear_data_download(browser)

    @pytestrail.case('C96719')
    def test_download_youtube(self, browser, get_current_download_folder):
        self.implement_test_site(browser, VideoUrls.YOUTUBE_VIDEO_URL, get_current_download_folder)

    @pytestrail.case('C96752')
    def test_download_news_zing(self, browser, get_current_download_folder):
        self.implement_test_site(browser, VideoUrls.NEWS_ZING_VIDEO_URL, get_current_download_folder)

    @pytestrail.case('C96756')
    def test_download_zing_mp3_vn(self, browser, get_current_download_folder):
        self.implement_test_site(browser, VideoUrls.ZING_MP3_VN_VIDEO_URL, get_current_download_folder)

    @pytestrail.case('C96758')
    def test_download_nhaccuatui(self, browser, get_current_download_folder):
        self.implement_test_site(browser, VideoUrls.NHAC_CUA_TUI_VIDEO_ITEM, get_current_download_folder)

    @pytestrail.case('C98735')
    def test_download_dongphim(self, browser, get_current_download_folder):
        self.implement_test_site(browser, VideoUrls.DONG_PHIM_VIDEO_URL, get_current_download_folder)


