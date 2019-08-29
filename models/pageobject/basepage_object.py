from datetime import datetime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from models.pagelocators.savior import SaviorPageLocators
from utils_automation.common import WebElements
from utils_automation.setup import WaitAfterEach
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.mojichat import MojichatLocators
from utils_automation.setup import WaitAfterEach


class BasePageObject(object):

    def wait_until_document_ready(self, driver):
        wait_document_ready = WebDriverWait(driver, 60)
        wait_document_ready.until(lambda driver1: driver.execute_script("return document.readyState") == "complete")

    def send_keys_to_element(self, driver, element, keys):
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys(keys)
        actions.perform()

    def clear_text_to_element(self, driver, element):
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys(Keys.CONTROL + "a")
        actions.send_keys(Keys.DELETE)
        actions.perform()

    def get_text_element(self, element):
        return element.get_attribute('innerHTML')

    def press_arrow_up(self, driver, loop=1):
        for i in range(loop):
            driver.find_element_by_css_selector('body').send_keys(Keys.ARROW_UP)
            WaitAfterEach.sleep_timer_after_each_step()

    def verify_savior_popup_appear(self, driver):
        return driver.execute_script('return document.querySelector(arguments[0]).'
                                     'shadowRoot.querySelector(arguments[1])', SaviorPageLocators.FIRST_LAYER,
                                     SaviorPageLocators.DOWNLOAD_BUTTON)

    def mouse_over_video_element_site(self, driver, element):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        start_time = datetime.now()
        while self.verify_savior_popup_appear(driver) is None:
            WebElements.mouse_over_element(driver, element)
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 10:
                break




