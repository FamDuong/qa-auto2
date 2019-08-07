from selenium.common.exceptions import StaleElementReferenceException

from models.pageelements.savior import SaviorElements
from models.pagelocators.savior import SaviorPageLocators
from models.pageobject.basepage_object import BasePageObject


class SaviorPageObject(BasePageObject):
    savior_elements = SaviorElements()
    script = 'document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).click();'

    def download_button_is_displayed(self, driver):
        self.savior_elements.find_download_button(driver)

    def not_found_download_button(self, driver):
        self.savior_elements.not_found_download_button(driver)

    def choose_preferred_option(self, driver):
        driver.execute_script(
                 self.script,
                 SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.PREFFERED_SELECT_BTN)

    def choose_medium_option(self, driver):
        driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MEDIUM_SELECT_OPTION)

    def assert_value_preferred_quality(self, driver, assert_text):
        preferred_element = driver.execute_script('return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).getAttribute("data-selected-value")',
                              SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.PREFFERED_SELECT_BTN)
        assert preferred_element == assert_text

