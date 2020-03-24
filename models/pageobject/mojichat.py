import time
from datetime import datetime

import pytest
from selenium import webdriver

from models.pagelocators.extensions import MojiChatLocators
from models.pagelocators.facebook import FacebookPageLocators, FacebookMessagePageLocators
from models.pagelocators.flags import FlagsPageLocators
from models.pageobject.settings import SettingsPageObject
from testscripts.smoketest.common import chrome_options_preset
from utils_automation.setup import WaitAfterEach
from utils_automation.const import Urls, OtherSiteUrls
from models.pageobject.basepage_object import BasePageObject
from models.pagelocators.mojichat import MojichatLocators
from models.pageelements.mojichat import MojichatElement, ChatElement
from models.pageobject.extensions import ExtensionsPageObject, ExtensionsDetailsPageObject
import time
import pytest
from models.pagelocators.mojichat import MojichatLocators
from utils_automation.common import CSVHandle, WebElements
from testscripts.smoketest.common import cleanup
from models.pagelocators.flags import FlagsPageLocators


class MojichatObjects(BasePageObject):
    settings_page_object = SettingsPageObject()
    extensions_page_object = ExtensionsPageObject()
    extensions_details_page_object = ExtensionsDetailsPageObject()
    mojichat_element = MojichatElement()
    chat_element = ChatElement()

    # mojichat_element = MojichatElement(self.chat_type)

    # def __init__(self, type=MojichatLocators.BIG_CHAT):
    #     self.chat_type = type
    #     self.mojichat_element = MojichatElement(self.chat_type)

    def open_chat_browser(self, browser, chat_type):
        if chat_type in 'BIG_CHAT':
            browser.get(Urls.MESSENDER_URL)
            continue_as_user_btn = browser.find_elements_by_xpath(
                FacebookMessagePageLocators.CONTINUE_WITH_USER_BTN_XPATH)
            if len(continue_as_user_btn) == 1:
                browser.find_element_by_xpath(FacebookMessagePageLocators.CONTINUE_WITH_USER_BTN_XPATH).click()

        elif chat_type in 'SMALL_CHAT':
            browser.get(Urls.FACEBOOK_URL)
            coccoc_at_user_lbl = browser.find_elements_by_xpath(FacebookPageLocators.COCCOC_AT_NAME_XPATH)
            if len(coccoc_at_user_lbl) == 0:
                self.login_facebook(browser)
            browser.find_element_by_xpath(FacebookPageLocators.FACEBOOK_MESSAGE_SMALL_ICON_XPATH).click()
            time.sleep(2)
            browser.find_element_by_xpath(FacebookPageLocators.USER_NAME_ON_CHAT_TOOL_TIP_XPATH).click()

        elif chat_type in 'BIG_CHAT_FACEBOOK_MESSENDER':
            browser.get(Urls.FACEBOOK_MESSENDER_URL)

    # def click_moji_on_suggestion_panel(self, driver, position):
    #     element = self.mojichat_element.find_moji_on_suggestion_panel(driver, position)
    #     element.click()
    #
    # def clear_text_into_chat_box(self, driver):
    #     element = self.mojichat_element.find_big_chat_input(driver)
    #     return self.clear_text_to_element(driver, element)
    #     # WaitAfterEach.sleep_timer_after_each_step()
    #

    # def select_user_chat(self, driver, user_chat):
    #     element = self.mojichat_element.find_user_chat(driver, user_chat)
    #     element.click()
    #     self.user_chat = user_chat
    #     WaitAfterEach.sleep_timer_after_each_step()
    #

    #
    # def select_moji_on_suggestion_panel(self, driver, chat_text, position):
    #     # self.clear_text_into_chat_box(driver)
    #     self.input_text_into_chat(driver, chat_text)
    #     self.click_moji_on_suggestion_panel(driver, position)
    #     # self.click_on_send_button(driver)
    #
    # def select_moji_on_suggestion_panel_by_arrow_key(self, driver, chat_text, position):
    #     self.input_text_into_chat(driver, chat_text)
    #     self.press_arrow_up(driver)
    #
    # def verify_chat_is_empty(self, driver):
    #     # Keyword is auto-deleted after user sends the sticker
    #     element = self.mojichat_element.find_chat_input(driver)
    #     chat = self.get_text_element(element)
    #     assert chat == ""

    def logout_facebook(self, driver):
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
                show_menu_setting_icon = driver.find_elements_by_xpath(
                    FacebookPageLocators.SHOW_MENU_SETTING_ICON_XPATH)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 15:
                    break

    def on_off_moji_extension(self, driver, action='ON'):
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

    def verify_moji_icon_is_on(self, driver, chat_type, moji_is_on=True):
        self.open_chat_browser(driver, chat_type)
        moji_icon = driver.find_elements_by_xpath(MojichatLocators.MOJI_ICON)
        if moji_is_on:
            assert len(moji_icon) == 1
        else:
            assert len(moji_icon) == 0

    def on_off_moji_in_detail_extension_page(self, driver):
        self.settings_page_object.enable_extension_toggle_dev_mode(driver)
        self.extensions_page_object.click_extension_detail_button(driver, MojiChatLocators.MOJICHAT_ID)
        self.extensions_details_page_object.on_off_extension_in_detail_page(driver, is_on_extension=False)

    def verify_send_first_sticker(self, driver, chat_type):
        self.open_chat_browser(driver, chat_type)
        self.input_keyword_then_verify_sticker_suggestion_and_tooltip(driver, chat_type)
        self.send_sticker_then_verify_thankyou_popup(driver, chat_type)
        self.close_thank_you_popup_then_verify_it_closed(driver, chat_type)

    # def send_text_into_chat(self, driver, chat_text):
    #     self.input_text_into_chat(driver, chat_text)
    #     self.click_on_send_button(driver)

    def input_text_into_chat(self, driver, chat_text):
        element = self.chat_element.find_chat_input(driver)
        return self.send_keys_to_element(driver, element, chat_text)

    # def click_on_send_button(self, driver):
    #     try:
    #         if (self.chat_type == MojichatLocators.BIG_CHAT):
    #             locator = MojichatLocators.BIG_CHAT_BTN_SEND
    #         elif (self.chat_type == MojichatLocators.SMALL_CHAT):
    #             locator = MojichatLocators.SMALL_CHAT_BTN_SEND
    #         element = self.mojichat_element.find_tooltip_button(driver, locator)
    #         element.click()
    #         WaitAfterEach.sleep_timer_after_each_step()
    #     except Exception as e:
    #         print("Not found button Send")

    def input_keyword_then_verify_sticker_suggestion_and_tooltip(self, driver, chat_type):
        # Input keyword
        if chat_type in 'SMALL_CHAT':
            WebElements.click_element_by_javascript(driver, self.mojichat_element.find_de_xem_nao_btn(driver))
        WebElements.click_element_by_javascript(driver, self.mojichat_element.find_de_go_thu_btn(driver))
        self.mojichat_object.input_text_into_chat(driver, "hihi")

        # Verify suggestion and tooltip
        assert 'Click vào hình để gửi nhé' in self.mojichat_element.find_click_vao_hinh_de_gui_nhe_tool_tip(driver).text

        if chat_type in 'SMALL_CHAT':
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 1).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 2).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 3).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 4).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 5).get_attribute('keyword')
            assert self.mojichat_element.find_sticker_by_index(driver, chat_type, 0) is None
            assert self.mojichat_element.find_sticker_by_index(driver, chat_type, 6) is None
        elif chat_type in 'BIG_CHAT':
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 1).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 2).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 3).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 4).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 5).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 6).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 7).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 8).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 9).get_attribute('keyword')
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, chat_type, 10).get_attribute('keyword')
            assert self.mojichat_element.find_sticker_by_index(driver, chat_type, 0) is None
            assert self.mojichat_element.find_sticker_by_index(driver, chat_type, 11) is None

    def send_sticker_then_verify_thankyou_popup(self, driver, chat_type):
        WebElements.click_element_by_javascript(driver,
                                                self.mojichat_element.find_sticker_by_index(driver, chat_type, 1))
        assert 'Chúc mừng bạn đã gửi sticker thành công' in self.mojichat_element.find_thank_you_popup(driver,
                                                                                                       chat_type).text

    def close_thank_you_popup_then_verify_it_closed(self, driver, chat_type):
        WebElements.click_element_by_javascript(driver, self.mojichat_element.find_da_hieu_btn(driver))
        assert self.mojichat_element.find_thank_you_popup(driver, chat_type) is None

    # def change_moji_flag_status(self, status='Enabled'):
    #     from testscripts.smoketest.common import cleanup
    #     cleanup()
    #     driver = webdriver.Chrome(options=chrome_options_preset())
    #     driver.get(Urls.COCCOC_FLAGS)
    #     driver.find_element_by_id(FlagsPageLocators.SEARCH_FLAG_TXT_ID).send_keys('MojiChat Extension')
    #     from selenium.webdriver.support.select import Select
    #     status_ddl = Select(driver.find_element_by_xpath(FlagsPageLocators.STATUS_DDL_XPATH))
    #     if status_ddl.first_selected_option.text not in status:
    #         status_ddl.select_by_visible_text(status)
    #         # time.sleep(2)
    #         # browser.find_element_by_id(FlagsPageLocators.RELAUNCH_BTN_ID).click()
    #         time.sleep(3)
    #         from testscripts.smoketest.common import cleanup
    #         cleanup()
    #
    # def open_browser_by_cmd(self):
    #     from utils_automation.common import WindowsHandler
    #     windows_handler = WindowsHandler()
    #     current_user = windows_handler.get_current_login_user()
    #     import subprocess
    #     subprocess.Popen(["powershell.exe",
    #                       f"C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe", ],
    #                      shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     time.sleep(4)
    #     from testscripts.smoketest.common import cleanup
    #     cleanup()
    #     time.sleep(3)
    #
    # def open_coccoc_extensions_page(self):
    #     driver = webdriver.Chrome(options=chrome_options_preset())
    #     from utils_automation.const import Urls
    #     driver.get(Urls.COCCOC_VERSION_URL)
    #     driver.get(Urls.COCCOC_SETTINGS_URL)
    #     driver.get(Urls.COCCOC_EXTENSIONS)
    #
    # def enable_moji(self):
    #     self.change_moji_flag_status()
    #     self.open_browser_by_cmd()
    #     self.open_coccoc_extensions_page()
