import pytest

from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import implement_download_file, \
    clear_data_download_in_browser_and_download_folder, verify_video_step_then_clear_data
from utils_automation.const import OtherSiteUrls


any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()


class TestFacebook:

    @pytestrail.case('C96691')
    @pytest.mark.ten_popular_sites
    def test_download_file_facebook(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.FACEBOOK_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_facebook(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestMessenger:

    @staticmethod
    def setup_savior_option_appear(driver):
        driver.get(OtherSiteUrls.MESSENGER_CHAT_URL)
        any_site_page_object.click_video_element_messenger_chat(driver)
        any_site_page_object.mouse_over_video_element_messenger_chat(driver)

    @pytestrail.case('C96722')
    def test_download_file_messenger(self, browser, get_current_download_folder):
        self.setup_savior_option_appear(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestInstagram:

    @staticmethod
    def prepare_appear_savior_option(browser):
        browser.get(OtherSiteUrls.INSTAGRAM_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_instagram(browser)

    @pytestrail.case('C96751')
    def test_download_file_instagram(self, browser, get_current_download_folder):
        self.prepare_appear_savior_option(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestTwitter:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.TWITTER_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_twitter(browser)

    @pytestrail.case('C98721')
    @pytestrail.defect('PF-467')
    def test_download_file_twitter(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestWeibo:

    @pytestrail.case('C98802')
    def test_download_file_weibo(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.WEIBO_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_weibo(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))




