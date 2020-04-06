import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from models.pageelements.top_savior_sites.top_savior_sites_social import MessengerElements
from models.pageobject.basepage_object import BasePageObject


class MessengerActions(BasePageObject):
    messenger_element = MessengerElements()

    def get_number_of_login_elements(self, driver: WebDriver):
        time.sleep(1)
        return len(self.messenger_element.find_login_button_element_by_find_elements(driver))

    def input_email_phone_number_into_email_text_box(self, driver: WebDriver, text):
        email_text_box: WebElement = self.messenger_element.find_email_text_box(driver)
        email_text_box.click()
        email_text_box.clear()
        email_text_box.send_keys(text)

    def input_password_into_password_text_box(self, driver: WebDriver, text):
        password_text_box: WebElement = self.messenger_element.find_password_text_box(driver)
        password_text_box.click()
        password_text_box.clear()
        password_text_box.send_keys(text)

    def click_login_button(self, driver: WebDriver):
        login_button: WebElement = self.messenger_element.find_login_button(driver)
        login_button.click()

    def login_messenger_task(self, driver: WebDriver, email_or_phone_info=None, password_info=None):
        self.input_email_phone_number_into_email_text_box(driver, email_or_phone_info)
        self.input_password_into_password_text_box(driver, password_info)
        self.click_login_button(driver)






