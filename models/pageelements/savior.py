import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.savior import SaviorPageLocators


class SaviorElements(BasePageElement):

    def find_first_layer(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, SaviorPageLocators.FIRST_LAYER)))

    def select_shadow_element_savior(self, driver, element1, element2):
        try:
            element = driver.execute_script(
                'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1])',
                element1, element2)
            return element
        except:
            return 1

    def select_shadow_element_savior_only_root(self, driver):
        return driver.execute_script('return document.querySelector(arguments[0]).shadowRoot',SaviorPageLocators.FIRST_LAYER)

    def select_shadow_element_download_button(self, driver):
        return self.select_shadow_element_savior(driver, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.DOWNLOAD_BUTTON)

    def select_shadow_element_preferred_select(self, driver):
        return self.select_shadow_element_savior(driver, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.PREFFERED_SELECT_BTN)

    def find_download_button(self, driver):
        return self.select_shadow_element_download_button(driver)

    def not_found_download_button(self, driver):
        print('Value for assertions isssss:', self.select_shadow_element_download_button(driver))
        assert self.select_shadow_element_download_button(driver) in (1, None)

    def find_preferred_option(self, driver):
        return self.select_shadow_element_by_css_selector(driver, self.find_first_layer(driver)).find_element_by_css_selector(SaviorPageLocators.PREFFERED_SELECT_BTN)
