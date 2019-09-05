from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import implement_download_file, \
    clear_data_download_in_browser_and_download_folder
from utils_automation.const import OtherSiteUrls


any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()


class TestFacebook:

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        browser.get(OtherSiteUrls.FACEBOOK_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_facebook(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')


class TestMessenger:

    @staticmethod
    def setup_savior_option_appear(driver):
        driver.get(OtherSiteUrls.MESSENGER_CHAT_URL)
        any_site_page_object.click_video_element_messenger_chat(driver)
        any_site_page_object.mouse_over_video_element_messenger_chat(driver)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.setup_savior_option_appear(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_click_download_video_messenger(self, browser, get_current_download_folder):
        self.setup_savior_option_appear(browser)
        try:
            implement_download_file(browser, get_current_download_folder)
        finally:
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)


class TestInstagram:

    @staticmethod
    def prepare_appear_savior_option(browser):
        browser.get(OtherSiteUrls.INSTAGRAM_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_instagram(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.prepare_appear_savior_option(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_click_download_video_item(self, browser, get_current_download_folder):
        self.prepare_appear_savior_option(browser)
        try:
            implement_download_file(browser, get_current_download_folder)
        finally:
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)


class TestTwitter:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.TWITTER_VIDEO_URL)
        any_site_page_object.choose_media_view_option_twitter(browser)
        any_site_page_object.mouse_over_video_item_twitter(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.prepare_savior_option_appear(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_click_download_video_item(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        try:
            implement_download_file(browser, get_current_download_folder)
        finally:
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)



