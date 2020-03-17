import time

import pytest

from pytest_testrail.plugin import pytestrail
from models.pageobject.mojichat import MojichatObjects
from models.pagelocators.mojichat import MojichatLocators
from utils_automation.setup import Browser
from utils_automation.common import CSVHandle
from utils_automation.const import Urls
from testscripts.smoketest.common import coccoc_instance, wait_for_element_is_exist
from models.pageelements.version import VersionPageElements
from models.pagelocators.flags import FlagsPageLocators
from models.pagelocators.facebook import FacebookPageLocators

browser = Browser()
user_chat = "Coc Coc"
mojichat_file = "mojichat_list.csv"


# @pytest.mark.skip(reason='Skip mojchat')
class TestSuggestionPanelBigBoxChat:
    mojichat_object = MojichatObjects()
    version_page_element = VersionPageElements()

    def enable_moji(self, driver):
        #driver = coccoc_instance()
        driver.get(Urls.COCCOC_FLAGS)
        driver.find_element_by_id(FlagsPageLocators.SEARCH_FLAG_TXT_ID).send_keys('MojiChat Extension')
        from selenium.webdriver.support.select import Select
        status_ddl = Select(driver.find_element_by_xpath(FlagsPageLocators.STATUS_DDL_XPATH))
        status_ddl.select_by_visible_text("Enabled")
        time.sleep(2)
        driver.find_element_by_id(FlagsPageLocators.RELAUNCH_BTN_ID).click()

    def logout_facebook(self, driver):
        driver.get(Urls.FACEBOOK_URL)
        driver.find_element_by_id(FacebookPageLocators.SHOW_MENU_SETTING_ICON_ID).click()
        wait_for_element_is_exist(driver.find_element_by_xpath(FacebookPageLocators.LOGOUT_BTN_XPATH))
        driver.find_element_by_xpath(FacebookPageLocators.LOGOUT_BTN_XPATH).click()

    def test_login_facebook(self):
        driver = coccoc_instance()
        driver.get(Urls.FACEBOOK_URL)
        show_menu_setting_icon = driver.find_elements_by_id(FacebookPageLocators.SHOW_MENU_SETTING_ICON_ID)
        if len(show_menu_setting_icon) == 1:
            self.logout_facebook(driver)
        driver.find_element_by_id(FacebookPageLocators.EMAIL_TXT_ID).send_keys(FacebookPageLocators.EMAIL)
        driver.find_element_by_id(FacebookPageLocators.PASS_TXT_ID).send_keys(FacebookPageLocators.PASS)
        driver.find_element_by_id(FacebookPageLocators.SUBMIT_BTN_ID).click()


    def test_status_change_when_user_turn_on_off_moji_feature(self):
        self.enable_moji()
        driver = coccoc_instance()
        driver.get(Urls.COCCOC_EXTENSIONS)

    @pytestrail.case('C54462')
    def test_check_if_suggestion_is_shown_when_entering_the_supported_keyword(self, browser):
        self.mojichat_object.open_chat_browser(browser)
        self.mojichat_object.select_user_chat(browser, user_chat)
        self.mojichat_object.send_text_into_chat(browser, "clear cache")

        list_mojichat = CSVHandle().get_from_csv(mojichat_file)
        for i in list_mojichat:
            self.mojichat_object.select_moji_on_suggestion_panel(browser, i, 0)
            self.mojichat_object.verify_chat_is_empty(browser)

    @pytestrail.case('C86095')
    def test_check_if_user_can_using_arrow_key_to_navigate_suggestion_stickers(self, browser):
        self.mojichat_object.open_chat_browser(browser)
        self.mojichat_object.select_user_chat(browser, user_chat)
        self.mojichat_object.select_moji_on_suggestion_panel_by_arrow_key(browser, "hihi")
        time.sleep(10)


@pytest.mark.skip(reason='Skip mojchat')
class TestSuggestionPanelSmallChat:
    mojichat_object = MojichatObjects(MojichatLocators.SMALL_CHAT)

    @pytestrail.case('C54462')
    def test_check_if_suggestion_is_shown_when_entering_the_supported_keyword(self, browser):
        self.mojichat_object.open_chat_browser(browser)
        self.mojichat_object.select_user_chat(browser, user_chat)
        self.mojichat_object.send_text_into_chat(browser, "clear cache")

        list_mojichat = CSVHandle().get_from_csv(mojichat_file)
        for i in list_mojichat:
            self.mojichat_object.select_moji_on_suggestion_panel(browser, i, 0)
            self.mojichat_object.verify_chat_is_empty(browser)
