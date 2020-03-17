import traceback
from utils_automation.setup import Browser, WaitAfterEach
from utils_automation.const import Urls, OtherSiteUrls
from models.pageobject.basepage_object import BasePageObject
from models.pagelocators.mojichat import MojichatLocators
from models.pageelements.mojichat import MojichatElement

class MojichatObjects(BasePageObject):
    # mojichat_element = MojichatElement(self.chat_type)

    def __init__(self, type = MojichatLocators.BIG_CHAT):
        self.chat_type = type
        self.mojichat_element = MojichatElement(self.chat_type)

    def open_chat_browser(self, browser):
        if (self.chat_type == MojichatLocators.BIG_CHAT):
            browser.get(OtherSiteUrls.MOJI_BIG_CHATBOX)
        else:
            browser.get(Urls.FACEBOOK_URL)
            element = self.mojichat_element.find_small_chat_icon(browser)
            element.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def click_on_send_button(self, driver):
        try:
            if (self.chat_type == MojichatLocators.BIG_CHAT):
                locator = MojichatLocators.BIG_CHAT_BTN_SEND
            elif (self.chat_type == MojichatLocators.SMALL_CHAT):
                locator = MojichatLocators.SMALL_CHAT_BTN_SEND
            element = self.mojichat_element.find_tooltip_button(driver, locator)
            element.click()
            WaitAfterEach.sleep_timer_after_each_step()
        except Exception as e: print("Not found button Send")

    def click_moji_on_suggestion_panel(self, driver, position):
        element = self.mojichat_element.find_moji_on_suggestion_panel(driver, position)
        element.click()


    def clear_text_into_chat_box(self, driver):
        element = self.mojichat_element.find_big_chat_input(driver)
        return self.clear_text_to_element(driver, element)
        # WaitAfterEach.sleep_timer_after_each_step()

    def input_text_into_chat(self, driver, chat_text):
        element = self.mojichat_element.find_chat_input(driver)
        return self.send_keys_to_element(driver, element, chat_text)

    def select_user_chat(self, driver, user_chat):
        element = self.mojichat_element.find_user_chat(driver, user_chat)
        element.click()
        self.user_chat = user_chat
        WaitAfterEach.sleep_timer_after_each_step()

    def send_text_into_chat(self, driver, chat_text):
        self.input_text_into_chat(driver, chat_text)
        self.click_on_send_button(driver)

    def select_moji_on_suggestion_panel(self, driver, chat_text, position):
        # self.clear_text_into_chat_box(driver)
        self.input_text_into_chat(driver, chat_text)
        self.click_moji_on_suggestion_panel(driver, position)
        # self.click_on_send_button(driver)

    def select_moji_on_suggestion_panel_by_arrow_key(self, driver, chat_text, position):
        self.input_text_into_chat(driver, chat_text)
        self.press_arrow_up(driver)

    def verify_chat_is_empty(self, driver):
        # Keyword is auto-deleted after user sends the sticker
        element = self.mojichat_element.find_chat_input(driver)
        chat = self.get_text_element(element)
        assert chat == ""








