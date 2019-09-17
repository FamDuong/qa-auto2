from pytest_testrail.plugin import pytestrail

from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from testscripts.sanitytest.savior.common_setup import verify_video_step_then_clear_data, implement_download_file, \
    clear_data_download_in_browser_and_download_folder
from utils_automation.const import OtherSiteUrls


any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()


class TestXVideos:

    @pytestrail.case('C96723')
    def test_download_file_x_videos(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.XVIDEOS_DOT_COM_VIDEO_URL)
        any_site_page_object.mouse_over_video_x_videos(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestXNXX:

    @pytestrail.case('C96754')
    def test_download_file_x_videos(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.XNXX_VIDEO_URL)
        any_site_page_object.mouse_over_video_xnxx(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestPornHub:

    @pytestrail.case('C98771')
    def test_download_file_x_videos(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.FR_PORN_HUB_VIDEO_URL)
        any_site_page_object.mouse_over_video_fr_porn_hub(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))