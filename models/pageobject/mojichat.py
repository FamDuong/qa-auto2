import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from models.pagelocators.extensions import MojiChatLocators
from models.pagelocators.facebook import FacebookPageLocators, FacebookMessagePageLocators
from models.pageobject.settings import SettingsPageObject
from utils_automation.setup import WaitAfterEach
from utils_automation.const import Urls
from models.pageobject.basepage_object import BasePageObject
from models.pageelements.mojichat import MojichatElement, ChatElement
from models.pageobject.extensions import ExtensionsPageObject, ExtensionsDetailsPageObject
from utils_automation.common import WebElements
from models.pagelocators.mojichat import MojichatLocators


class MojichatObjects(BasePageObject):
    settings_page_object = SettingsPageObject()
    extensions_page_object = ExtensionsPageObject()
    extensions_details_page_object = ExtensionsDetailsPageObject()
    mojichat_element = MojichatElement()
    chat_element = ChatElement()

    def open_chat_browser(self, browser, chat_type):
        browser.maximize_window()
        if chat_type in 'BIG_CHAT':
            browser.get(Urls.MESSENDER_URL)
            continue_as_user_btn = browser.find_elements_by_xpath(
                FacebookMessagePageLocators.CONTINUE_WITH_USER_BTN_XPATH)
            if len(continue_as_user_btn) == 1:
                browser.find_element_by_xpath(FacebookMessagePageLocators.CONTINUE_WITH_USER_BTN_XPATH).click()
        elif chat_type in 'SMALL_CHAT':
            browser.get(Urls.FACEBOOK_URL)
            browser.get(Urls.FACEBOOK_COC_COC_BAY_PROFILE_URL)
            browser.find_element_by_xpath(FacebookPageLocators.NHAN_TIN_BTN_XPATH).click()
        elif chat_type in 'BIG_CHAT_FACEBOOK_MESSENDER':
            browser.get(Urls.FACEBOOK_MESSENDER_URL)
        time.sleep(3)

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
            self.clear_text_to_element(driver, email_txt)
            self.send_keys_to_element(driver, email_txt, FacebookPageLocators.EMAIL)
            self.clear_text_to_element(driver, pass_txt)
            self.send_keys_to_element(driver, pass_txt, FacebookPageLocators.PASS)
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

    def input_text_into_chat(self, driver, chat_type, chat_text):
        chat_box = self.chat_element.find_chat_input(driver, chat_type)
        self.clear_text_to_element(driver, chat_box)
        self.send_keys_to_element(driver, chat_box, chat_text)

    def verify_sticker_suggestion(self, driver, chat_type):
        if chat_type in 'SMALL_CHAT':
            max_range = 6
        elif chat_type in 'BIG_CHAT':
            max_range = 11
        for i in range(1, max_range, 1):
            assert 'hihi' in self.mojichat_element.find_sticker_by_index(driver, index=i).get_attribute('keyword')

    def input_keyword_then_verify_sticker_suggestion_and_tooltip(self, driver, chat_type):
        # Input keyword
        if chat_type in 'SMALL_CHAT':
            WebElements.click_element_by_javascript(driver, self.mojichat_element.find_de_xem_nao_btn(driver))
        WebElements.click_element_by_javascript(driver, self.mojichat_element.find_de_go_thu_btn(driver, chat_type))
        self.input_text_into_chat(driver, chat_type, chat_text='hihi')

        # Verify suggestion and tooltip
        assert 'Click vào hình để gửi nhé' in self.mojichat_element.find_click_vao_hinh_de_gui_nhe_tool_tip(driver,
                                                                                                            chat_type).text
        self.verify_sticker_suggestion(driver, chat_type)

    def send_sticker_then_verify_thankyou_popup(self, driver, chat_type):
        WebElements.click_element_by_javascript(driver, self.mojichat_element.find_sticker_by_index(driver, index=2))
        assert 'Chúc mừng bạn đã gửi sticker thành công' in self.mojichat_element.find_thank_you_popup(driver,
                                                                                                       chat_type).text

    def click_on_send_button(self, driver):
        try:
            if (self.chat_type == MojichatLocators.BIG_CHAT):
                locator = MojichatLocators.BIG_CHAT_BTN_SEND
            elif (self.chat_type == MojichatLocators.SMALL_CHAT):
                locator = MojichatLocators.SMALL_CHAT_BTN_SEND
            element = self.mojichat_element.find_tooltip_button(driver, locator)
            element.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            print("Not found button Send")

    def click_moji_on_suggestion_panel(self, driver, position):
        element = self.mojichat_element.find_moji_on_suggestion_panel(driver, position)
        element.click()

    def delete_message_then_send_text_message(self, driver):
        # Delete message
        driver.get(Urls.FACEBOOK_URL)
        coccoc_at_user_lbl = driver.find_elements_by_xpath(FacebookPageLocators.COCCOC_AT_NAME_XPATH)
        if len(coccoc_at_user_lbl) == 0:
            self.login_facebook(driver)
        driver.find_element_by_xpath(FacebookPageLocators.FACEBOOK_MESSAGE_SMALL_ICON_XPATH).click()
        driver.find_element_by_xpath(FacebookMessagePageLocators.XEM_TAT_CA_TRONG_MESSAGE_BTN_XPATH).click()
        time.sleep(5)
        coccoc_account_test = driver.find_elements_by_xpath(FacebookMessagePageLocators.OPEN_MENU_XPATH)
        if len(coccoc_account_test) > 0:
            driver.find_element_by_xpath(FacebookMessagePageLocators.OPEN_MENU_XPATH).click()
            driver.find_element_by_xpath(FacebookMessagePageLocators.XOA_CUOC_TRO_TRUYEN_XPATH).click()
            driver.find_element_by_xpath(FacebookMessagePageLocators.XOA_CUOC_TRO_TRUYEN_CONFIRM_XPATH).click()
        # Send text message
        driver.get(Urls.FACEBOOK_COC_COC_BAY_PROFILE_URL)
        driver.find_element_by_xpath(FacebookPageLocators.NHAN_TIN_BTN_XPATH).click()
        chat_box = self.chat_element.find_chat_input(driver, chat_type='SMALL_CHAT')
        self.send_keys_to_element(driver, chat_box, keys='Xin chào')
        self.send_keys_to_element(driver, chat_box, keys=Keys.ENTER)
        time.sleep(2)

    def get_sticker_is_sent(self, driver):
        time.sleep(3)
        try:
            sticker_is_sent = driver.find_element_by_xpath(FacebookMessagePageLocators.SENT_STICKER_IMAGE).is_displayed()
        except:
            sticker_is_sent = driver.find_element_by_xpath(FacebookMessagePageLocators.SENT_STICKER_MOJI).is_displayed()
        return sticker_is_sent

    def select_sticker_in_show_more(self, driver, sticker_in_show_more):
        time.sleep(5)
        if sticker_in_show_more:
            self.mojichat_element.find_show_more_sticker_button(driver).click()
            self.mojichat_element.find_sticker_in_show_more_popup(driver).click()
        else:
            self.mojichat_element.find_sticker_by_index(driver, index=1).click()

    def verify_keyword_is_auto_deleted_after_user_sends_the_sticker(self, driver, chat_type,
                                                                    sticker_in_show_more=False):
        self.delete_message_then_send_text_message(driver)
        self.open_chat_browser(driver, chat_type)
        self.input_text_into_chat(driver, chat_type, chat_text='hihi')
        self.select_sticker_in_show_more(driver, sticker_in_show_more)
        self.verify_chat_is_empty(driver, chat_type)
        assert self.get_sticker_is_sent(driver) is True

    def select_moji_on_suggestion_panel(self, driver, chat_type, chat_text, position):
        self.input_text_into_chat(driver, chat_type, chat_text)
        time.sleep(3)
        self.click_moji_on_suggestion_panel(driver, position)

    def verify_chat_is_empty(self, driver, chat_type):
        # Keyword is auto-deleted after user sends the sticker
        element = self.chat_element.find_chat_input(driver, chat_type)
        chat = self.get_text_element(element)
        assert chat == ""

    def click_on_send_button(self, driver):
        try:
            if self.chat_type == "BIG _CHAT":
                locator = MojichatLocators.BIG_CHAT_BTN_SEND
            elif self.chat_type == "SMALL_CHAT":
                locator = MojichatLocators.SMALL_CHAT_BTN_SEND
            element = self.mojichat_element.find_tooltip_button(driver, locator)
            WebElements.click_element_by_javascript(driver, element)
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e:
            print("Not found button Send")
