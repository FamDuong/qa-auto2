import time

import pytest
from models.pageobject.downloads import DownloadsPageObject
from models.pageobject.extensions import ExtensionsPageObject, ExtensionsDetailsPageObject, \
    SaviorExtensionOptionsPageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import YoutubePageObject, GooglePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import pause_any_video_youtube
from utils_automation.const import Urls
from utils_automation.setup import Browser


class TestSaviorSettings:
    extension_page_object = ExtensionsPageObject()

    extension_detail_page_object = ExtensionsDetailsPageObject()
    youtube_page_object = YoutubePageObject()
    savior_page_object = SaviorPageObject()

    browser_incognito = Browser()
    savior_extension = SaviorExtensionOptionsPageObject()
    google_page_object = GooglePageObject()

    download_page_object = DownloadsPageObject()

    def navigate_savior_details(self,browser):
        browser.get(Urls.COCCOC_EXTENSIONS)
        self.extension_page_object.savior_extension_is_displayed(browser)
        self.extension_page_object.savior_extension_detail_is_clicked(browser)

    def check_instant_download(self, browser, text):
        browser.get(u'chrome-extension://' + text + u'/options.html')
        self.savior_extension.choose_show_instant_download_youtube(browser)
        # self.savior_extension.choose_save_and_close_button(browser)

    def not_found_download_button_in_page(self, browser):
        self.youtube_page_object.choose_any_video_item(browser)
        self.youtube_page_object.mouse_over_video_item(browser)
        time.sleep(2)
        self.savior_page_object.not_found_download_button(browser)

    def get_text_extension_option(self, browser):
        self.navigate_savior_details(browser)
        time.sleep(1)
        self.extension_detail_page_object.open_extension_options_view(browser)
        time.sleep(1)
        return self.savior_extension.get_show_instant_download_youtube_value(browser)

    # def pause_any_video_youtube(self, browser):
    #     browser.get(Urls.YOUTUBE_URL)
    #     self.youtube_page_object.choose_any_video_item(browser)
    #     time.sleep(2)
    #     self.youtube_page_object.click_video_item(browser)
    #     time.sleep(1)

    @pytestrail.case('C54140')
    def test_default_status_savior_browser(self, browser):
        self.navigate_savior_details(browser)
        self.extension_detail_page_object.savior_button_is_enabled(browser)

    @pytestrail.case('C54141')
    def test_default_status_savior_incognito_window(self, browser):
        self.navigate_savior_details(browser)
        self.extension_detail_page_object.savior_incognito_is_disabled(browser)

        # Open another window browser
        browser_incognito = self.browser_incognito.browser_incognito()
        try:
            browser_incognito.get(Urls.YOUTUBE_URL)
            self.not_found_download_button_in_page(browser_incognito)
        finally:
            browser_incognito.quit()

    @pytest.mark.skip
    def test_simple(self, browser):
        browser.get(Urls.YOUTUBE_URL)
        self.youtube_page_object.choose_any_video_item(browser)
        self.youtube_page_object.mouse_over_video_item(browser)
        time.sleep(4)
        self.savior_page_object.download_button_is_displayed(browser)

    @pytestrail.case('C54142')
    def test_check_working_instant_download_youtube(self, browser):
        text = self.get_text_extension_option(browser)
        self.check_instant_download(browser, text)

        # Navigate to google for download
        try:
            browser.get(Urls.GOOGLE_URL)
            self.google_page_object.search_with_value(browser, 'du du du')
            self.google_page_object.search_result_video(browser)
            time.sleep(1)
            self.google_page_object.download_via_savior_icon_button(browser)
            time.sleep(5)

            # Go to download internal page
            browser.get(Urls.COCCOC_DOWNLOAD_URL)
            # Assertion
            self.download_page_object.verify_cancel_button_is_existed(browser)
        finally:
            # Clear data
            self.download_page_object.cancel_all_current_torrent(browser)
            self.download_page_object.clear_all_existed_torrent(browser)

    @pytest.mark.skip
    @pytestrail.case('C54143')
    def test_check_changing_default_value_option(self):
        pass

    @pytest.mark.skip
    @pytestrail.case('C54144')
    def test_quality_file_type_downloaded(self):
        pass

    @pytestrail.case('C54145')
    @pytest.mark.skip
    def test_check_download_media_one_click(self, browser):
        pass

    @pytestrail.case('C54146')
    def test_enable_disable_download_control(self, browser):
        text = self.get_text_extension_option(browser)
        browser.get(u'chrome-extension://' + text + u'/options.html')
        time.sleep(2)
        # Verify default value is enabled
        assert self.savior_extension.verify_show_download_button_near_is_checked(browser) == 'true'
        try:
            self.savior_extension.click_show_download_button_near(browser)
            assert self.savior_extension.verify_show_download_button_near_is_checked(browser) is None
            browser.get(Urls.YOUTUBE_URL)
            self.not_found_download_button_in_page(browser)
        finally:
            browser.get(u'chrome-extension://' + text + u'/options.html')
            time.sleep(1)
            self.savior_extension.click_show_download_button_near(browser)
            time.sleep(1)

    @pytestrail.case('C54147')
    def test_if_remember_last_chosen_quality(self, browser):
        text = self.get_text_extension_option(browser)
        browser.get(u'chrome-extension://' + text + u'/options.html')
        self.savior_extension.choose_video_quality_low(browser)
        self.savior_extension.choose_remember_last_chosen_option(browser)
        time.sleep(2)

        pause_any_video_youtube(browser, self.youtube_page_object)
        self.savior_page_object.choose_preferred_option(browser)
        time.sleep(3)

        self.savior_page_object.choose_medium_option(browser)
        time.sleep(1)
        # Assert value must be medium when choose another video
        pause_any_video_youtube(browser, self.youtube_page_object)
        self.savior_page_object.assert_value_preferred_quality(browser, 'Medium')
        time.sleep(2)

        # Assert value must be medium when go to savior extension
        browser.get(u'chrome-extension://' + text + u'/options.html')
        try:
            assert self.savior_extension.verify_video_quality_medium_is_checked(browser) == 'true'
            time.sleep(1)
        finally:
            self.savior_extension.choose_video_quality_low(browser)





