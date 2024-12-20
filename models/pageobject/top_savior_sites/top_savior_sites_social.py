import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from models.pageelements.top_savior_sites.top_savior_sites_social import MessengerElements, FacebookElements, \
    InstagramElements
from models.pageobject.basepage_object import BasePageObject
from utils_automation.common_browser import coccoc_instance
from utils_automation.const import OtherSiteUrls


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


class FacebookActions(BasePageObject):
    facebook_element = FacebookElements()

    def scroll_to_facebook_video(self, driver, url):
        element = self.facebook_element.find_facebook_first_video(driver, url)
        driver.execute_script("window.scrollBy(0, 2000);")
        if element is None:
            while element is None:
                element = self.facebook_element.find_facebook_first_video(driver, url)
                driver.execute_script("window.scrollBy(0, 2000);")
                if element is not None:
                    coordinates = element.location_once_scrolled_into_view  # returns dict of X, Y coordinates
                    driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
                    break

    def click_on_first_video(self, driver):
        driver.execute_script('arguments[0].click()', self.facebook_element.find_first_video(driver))


class InstagramActions(BasePageObject):
    instagram_element = InstagramElements()

    def scroll_to_instagram_video(self, driver):
        element = self.instagram_element.find_instagram_first_video(driver)
        # driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        driver.execute_script("arguments[0].scrollIntoView();", element)
        # from selenium.webdriver.common.action_chains import ActionChains
        # ActionChains(driver).move_to_element(element).perform()
        if element is None:
            while element is None:
                element = self.instagram_element.find_instagram_first_video(driver)
                driver.execute_script("arguments[0].scrollIntoView();", element)
                # ActionChains(driver).move_to_element(element).perform()
                if element is not None:
                    coordinates = element.location_once_scrolled_into_view  # returns dict of X, Y coordinates
                    driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
                    break