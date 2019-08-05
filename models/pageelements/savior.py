import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.savior import SaviorPageLocators


class SaviorElements(BasePageElement):

    def find_first_layer(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, SaviorPageLocators.FIRST_LAYER)))

    def select_shadow_element(self, driver):
        first_layer = "[style='position: absolute; top: 0px;']"
        second_layer = "#download-main"
        try:
            element = driver.execute_script('return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1])',
                                        first_layer, second_layer)
            return element
        except:
            return 1

    def find_download_button(self, driver):
        return self.select_shadow_element(driver)

    def not_found_download_button(self, driver):
        assert 1 == self.select_shadow_element(driver)
