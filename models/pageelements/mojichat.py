import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.mojichat import MojichatLocators
from utils_automation.setup import WaitAfterEach

class MojichatElement(BasePageElement):
    global chat_type

    def __init__(self, type = MojichatLocators.BIG_CHAT):
        self.chat_type = type

    def click_on_tooltip_button(self, driver, button):
        element = self.find_tooltip_button(driver, button)
        element.click()
        WaitAfterEach.sleep_timer_after_each_step()

    def find_tooltip_button(self, driver, button):
        wait = WebDriverWait(driver, 20)
        return wait.until(ec.presence_of_element_located(button))

    def find_moji_on_suggestion_panel(self, driver, position):
        wait = WebDriverWait(driver, 20)
        # document.querySelector('[class="chat-suggestion-container"]')
        # document.querySelector('[class="chat-suggestion-container"]').shadowRoot
        # document.querySelector('[class="chat-suggestion-container"]').shadowRoot.querySelector('#sticker-suggestion')
        shadow_root = wait.until(ec.presence_of_element_located(MojichatLocators.MOJI_SUGGESTION_PANEL))
        element = driver.execute_script('return arguments[0].shadowRoot', shadow_root)
        return element.find_elements_by_css_selector('#sticker-suggestion')[position]

    def find_chat_input(self, driver):
        wait = WebDriverWait(driver, 20)
        if (self.chat_type == MojichatLocators.BIG_CHAT):
            locator = MojichatLocators.BIG_CHAT_INPUT
        elif (self.chat_type == MojichatLocators.SMALL_CHAT):
            locator = MojichatLocators.SMALL_CHAT_INPUT
            # locator = (By.XPATH, '//div[@class="fbNubFlyoutOuter" and descendant::span[text()="Coc Coc"]]//*[@data-text="true"]')
        return wait.until(ec.presence_of_element_located(locator))

    def find_small_chat_icon(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(ec.presence_of_element_located(MojichatLocators.MESSAGE_FACEBOOK))

    def find_user_chat(self, driver, user_chat):
        wait = WebDriverWait(driver, 20)
        return wait.until(ec.presence_of_element_located((By.XPATH, '//span[contains(text(),"' + user_chat + '")]')))








