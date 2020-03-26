import time
import pytest
from pytest_testrail.plugin import pytestrail

from models.pageobject.mojichat import MojichatObjects
from models.pagelocators.mojichat import MojichatLocators
from utils_automation.setup import Browser
from utils_automation.common import CSVHandle
from utils_automation.const import Urls
from testscripts.smoketest.common import coccoc_instance, cleanup
from models.pageelements.version import VersionPageElements
from models.pagelocators.flags import FlagsPageLocators
from models.pagelocators.facebook import FacebookPageLocators, FacebookMessagePageLocators
from datetime import datetime

browser = Browser()
user_chat = "Coc Coc"
mojichat_file = "mojichat_list.csv"


# @pytest.mark.skip(reason='Skip mojchat')
class TestSuggestionPanelBigBoxChat:
    mojichat_object = MojichatObjects()
    version_page_element = VersionPageElements()

    # def count_element(self, driver, element, find_by):
    #     logout_btn_count = driver.find_elements_by_id(element)
    #     if find_by in 'ID':
    #         logout_btn_count = driver.find_elements_by_id(element)
    #     elif find_by in 'XPATH':
    #         logout_btn_count = driver.find_elements_by_xpath(element)
    #     return len(logout_btn_count)

    # def wait_until_element_is_visible(self, driver, find_by):
    #     logout_btn_count = find_by
    #     print("logout_btn_count1"+str(len(logout_btn_count)))
    #     start_time = datetime.now()
    #     while len(logout_btn_count) < 1:
    #         time.sleep(2)
    #         logout_btn_count = find_by
    #         print("logout_btn_count2" + str(len(logout_btn_count)))
    #         time_delta = datetime.now() - start_time
    #         if time_delta.total_seconds() >= 15:
    #             break
    #     return driver
    def change_moji_flag_status(self, status='Enabled'):
        driver = coccoc_instance()
        driver.get(Urls.COCCOC_FLAGS)
        driver.find_element_by_id(FlagsPageLocators.SEARCH_FLAG_TXT_ID).send_keys('MojiChat Extension')
        from selenium.webdriver.support.select import Select
        status_ddl = Select(driver.find_element_by_xpath(FlagsPageLocators.STATUS_DDL_XPATH))
        if status_ddl.first_selected_option.text not in status:
            status_ddl.select_by_visible_text(status)
            time.sleep(2)
            driver.find_element_by_id(FlagsPageLocators.RELAUNCH_BTN_ID).click()

    def logout_facebook(self, driver):
        # driver = coccoc_instance()
        # driver.get(Urls.FACEBOOK_URL)

        driver.find_element_by_id(FacebookPageLocators.COCCOC_AT_NAME_XPATH).click()
        logout_btn_count = driver.find_elements_by_xpath(FacebookPageLocators.LOGOUT_BTN_XPATH)

        start_time = datetime.now()
        while len(logout_btn_count) == 0:
            time.sleep(2)
            logout_btn_count = driver.find_elements_by_xpath(FacebookPageLocators.LOGOUT_BTN_XPATH)
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 15:
                break
        driver.find_element_by_xpath(FacebookPageLocators.LOGOUT_BTN_XPATH).click()

    def login_facebook(self, driver):
        #driver = coccoc_instance()
        driver.get(Urls.FACEBOOK_URL)
        coccoc_at_user_lbl = driver.find_elements_by_xpath(FacebookPageLocators.COCCOC_AT_NAME_XPATH)
        if len(coccoc_at_user_lbl) == 0:
            show_menu_setting_icon = driver.find_elements_by_xpath(FacebookPageLocators.SHOW_MENU_SETTING_ICON_XPATH)
            if len(show_menu_setting_icon) == 1:
                self.logout_facebook(driver)
            email_txt = driver.find_element_by_id(FacebookPageLocators.EMAIL_TXT_ID)
            pass_txt = driver.find_element_by_id(FacebookPageLocators.PASS_TXT_ID)
            from utils_automation.common import WebElements
            WebElements.enter_string_into_element(email_txt, FacebookPageLocators.EMAIL)
            WebElements.enter_string_into_element(pass_txt, FacebookPageLocators.PASS)
            driver.find_element_by_xpath(FacebookPageLocators.SUBMIT_BTN_XPATH).click()
            show_menu_setting_icon = driver.find_elements_by_xpath(FacebookPageLocators.SHOW_MENU_SETTING_ICON_XPATH)
            start_time = datetime.now()
            while len(show_menu_setting_icon) == 0:
                time.sleep(2)
                show_menu_setting_icon = driver.find_elements_by_xpath(FacebookPageLocators.SHOW_MENU_SETTING_ICON_XPATH)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 15:
                    break

    def on_off_moji_extension(self, action='ON'):
        driver = coccoc_instance()
        driver.get(Urls.COCCOC_EXTENSIONS)
        from models.pageelements.basepage_elements import BasePageElement
        from models.pagelocators.extensions import ExtensionsPageLocators, MojiChatLocators
        on_off_btn = BasePageElement().find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                                           ExtensionsPageLocators.ITEMS_LIST,
                                                           MojiChatLocators.MOJICHAT_ID,
                                                           MojiChatLocators.MOJICHAT_ON_OFF_ID)
        if action in 'ON':
            if on_off_btn.get_attribute('checked') is None:
                on_off_btn.click()
        elif action in 'OFF':
            if on_off_btn.get_attribute('checked'):
                on_off_btn.click()
        time.sleep(2)
        cleanup()

    def verify_moji_icon_in_message_dot_com(self, driver, moji_is_on=True):
        #driver = coccoc_instance()
        driver.get(Urls.MESSENDER_URL)
        # driver.find_element_by_xpath(FacebookMessagePageLocators.CONTINUE_WITH_USER_BTN_XPATH).click()
        moji_icon = driver.find_elements_by_xpath(MojichatLocators.MOJI_ICON)
        if moji_is_on:
            assert len(moji_icon) == 1
        else:
            assert len(moji_icon) == 0

    def verify_moji_icon_in_facebook_message_dot_com(self, driver, moji_is_on=True):
        #driver = coccoc_instance()
        driver.get(Urls.FACEBOOK_MESSENDER_URL)
        moji_icon = driver.find_elements_by_xpath(MojichatLocators.MOJI_ICON)
        if moji_is_on:
            assert len(moji_icon) == 1
        else:
            assert len(moji_icon) == 0

    def verify_moji_icon_in_small_chat(self, driver, moji_is_on=True):
        driver.get(Urls.FACEBOOK_URL)
        driver.find_element_by_xpath(FacebookPageLocators.FACEBOOK_MESSAGE_SMALL_ICON_XPATH).click()
        time.sleep(2)
        driver.find_element_by_xpath(FacebookPageLocators.USER_NAME_ON_CHAT_TOOL_TIP_XPATH).click()
        moji_icon = driver.find_elements_by_xpath(MojichatLocators.MOJI_ICON)
        if moji_is_on:
            assert len(moji_icon) == 1
        else:
            assert len(moji_icon) == 0

    def verify_show_moji_icon(self, action, moji_is_on):
        try:
            self.on_off_moji_extension(action)
            driver = coccoc_instance()
            self.login_facebook(driver)
            self.verify_moji_icon_in_message_dot_com(driver, moji_is_on)
            self.verify_moji_icon_in_facebook_message_dot_com(driver, moji_is_on)
            self.verify_moji_icon_in_small_chat(driver, moji_is_on)
        finally:
            cleanup()

    def test_status_change_when_user_turn_on_off_moji_feature(self):
        self.verify_show_moji_icon(action='ON', moji_is_on=True)
        self.verify_show_moji_icon(action='OFF', moji_is_on=False)
        # try:
        #     #self.change_moji_flag_status(status="Enabled")
        #     self.on_off_moji_extension(action='ON')
        #     driver = coccoc_instance()
        #     self.login_facebook(driver)
        #     self.verify_moji_icon_in_message_dot_com(driver)
        #     self.verify_moji_icon_in_facebook_message_dot_com(driver)
        #     self.verify_moji_icon_in_small_chat(driver)
        #
        #     self.on_off_moji_extension(action='OFF')
        #     driver = coccoc_instance()
        #     self.login_facebook(driver)
        #     self.verify_moji_icon_in_message_dot_com(driver, moji_is_on=False)
        #     self.verify_moji_icon_in_facebook_message_dot_com(driver, moji_is_on=False)
        #     self.verify_moji_icon_in_small_chat(driver, moji_is_on=False)
        # finally:
        #     cleanup()

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
