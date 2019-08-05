import time

import pytest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from models.pageelements.extensions import ExtensionsElement
from models.pagelocators.extensions import ExtensionsPageLocators
from models.pageobject.extensions import ExtensionsPageObject, ExtensionsDetailsPageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.youtube import YoutubePageObject
from pytest_testrail.plugin import pytestrail
from utils.const import Urls
from utils.setup import Browser


class TestSaviorSettings:
    extension_page_object = ExtensionsPageObject()

    extension_detail_page_object = ExtensionsDetailsPageObject()
    youtube_page_object = YoutubePageObject()
    savior_page_object = SaviorPageObject()

    browser_incognito = Browser()

    def navigate_savior_details(self,browser):
        browser.get(Urls.COCCOC_EXTENSIONS)
        self.extension_page_object.savior_extension_is_displayed(browser)
        self.extension_page_object.savior_extension_detail_is_clicked(browser)

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
        browser_incognito.get(Urls.YOUTUBE_URL)
        self.youtube_page_object.choose_any_video_item(browser_incognito)
        self.youtube_page_object.mouse_over_video_item(browser_incognito)
        time.sleep(2)
        self.savior_page_object.not_found_download_button(browser_incognito)
        browser_incognito.quit()

    @pytest.mark.skip
    def test_simple(self, browser):
        browser.get(Urls.YOUTUBE_URL)
        self.youtube_page_object.choose_any_video_item(browser)
        self.youtube_page_object.mouse_over_video_item(browser)
        time.sleep(4)
        self.savior_page_object.download_button_is_displayed(browser)
