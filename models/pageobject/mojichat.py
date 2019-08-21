import traceback
from utils_automation.setup import Browser, WaitAfterEach
from utils_automation.const import Urls
from models.pageobject.basepage_object import BasePageObject
from models.pagelocators.mojichat import MojichatLocators
from models.pageelements.mojichat import MojichatElement

class MojichatObjects(BasePageObject):
    mojichat_element = MojichatElement()

    def open_chat_browser(self, browser, chat_type):
        if (chat_type == MojichatLocators.BIG_CHAT):
            browser.get(Urls.MOJI_BIG_CHATBOX)
        else:
            browser.get(Urls.FACEBOOK_URL)
            element = self.mojichat_element.find_small_chat_icon(browser)
            element.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def open_big_chat_browser(self, browser):
        browser.get(Urls.MOJI_BIG_CHATBOX)
        WaitAfterEach.sleep_timer_after_each_step()

    def click_on_send_button(self, driver):
        try:
            element = self.mojichat_element.find_tooltip_button(driver, MojichatLocators.BIG_CHAT_BTN_SEND)
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


    def input_text_into_big_chat(self, driver, chat_text):
        element = self.mojichat_element.find_big_chat_input(driver)
        return self.send_keys_to_element(driver, element, chat_text)

    def input_text_into_small_chat(self, driver, chat_text):
        element = self.mojichat_element.find_big_chat_input(driver)
        return self.send_keys_to_element(driver, element, chat_text)

    def select_user_chat(self, driver, user_chat):
        element = self.mojichat_element.find_user_chat(driver, user_chat)
        element.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def send_text_into_big_chat(self, driver, chat_text):
        # self.clear_text_into_chat_box(driver)
        self.input_text_into_big_chat(driver, chat_text)
        self.click_on_send_button(driver)

    def send_text_into_small_chat(self, driver, chat_text):
        # self.clear_text_into_chat_box(driver)
        self.input_text_into_small_chat(driver, chat_text)
        self.click_on_send_button(driver)

    def select_moji_on_suggestion_panel(self, driver, chat_type, chat_text, position):
        # self.clear_text_into_chat_box(driver)
        self.input_text_into_big_chat(driver, chat_text)
        self.click_moji_on_suggestion_panel(driver, position)
        # self.click_on_send_button(driver)

    def open_small_chat_browser(self, browser):
        browser.get(Urls.FACEBOOK_URL)
        element = self.mojichat_element.find_small_chat_icon(browser)
        element.click()







