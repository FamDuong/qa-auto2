import time

from selenium.common.exceptions import StaleElementReferenceException

from models.pageelements.savior import SaviorElements
from models.pagelocators.savior import SaviorPageLocators
from models.pageobject.basepage_object import BasePageObject


class SaviorPageObject(BasePageObject):
    savior_elements = SaviorElements()
    script = 'document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).click();'
    script_textContent = 'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).' \
                         'textContent'

    def download_button_is_displayed(self, driver):
        self.savior_elements.find_download_button(driver)

    def not_found_download_button(self, driver):
        self.savior_elements.not_found_download_button(driver)

    def choose_preferred_option(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.PREFFERED_SELECT_BTN)
        time.sleep(3)

    def choose_medium_option(self, driver):
        driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MEDIUM_SELECT_OPTION)
        time.sleep(2)

    def choose_low_option(self, driver):
        driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.LOW_SELECT_OPTION)
        time.sleep(2)

    def choose_high_option(self, driver):
        driver.execute_script(self.script, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.HIGH_SELECT_OPTION)
        time.sleep(2)

    def assert_value_preferred_quality(self, driver, assert_text):
        preferred_element = driver.execute_script(
            'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).getAttribute('
            '"data-selected-value")',
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.PREFFERED_SELECT_BTN)
        assert preferred_element == assert_text

    def download_file_via_savior_download_btn(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.DOWNLOAD_BUTTON)

    def download_file_medium_quality(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MEDIUM_FILE_DOWNLOAD_BUTTON)

    def download_file_high_quality(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.HIGH_FILE_DOWNLOAD_BUTTON)

    def download_file_low_quality(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.LOW_FILE_DOWNLOAD_BUTTON)

    def verify_mobile_sharing_button_displayed(self, driver):
        return driver.execute_script(
            self.script_textContent,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MOBILE_SHARING_BUTTON)

    def choose_mobile_sharing_button(self, driver):
        driver.execute_script(
            self.script,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MOBILE_SHARING_BUTTON)
        time.sleep(2)

    def verify_if_video_is_focused(self, driver):
        return driver.execute_script(
            'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).getAttribute('
            '"checked")',
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MOBILE_SHARING_VIDEO_RADIO_BUTTON)

    def verify_instruction_image_part_displayed(self, driver):
        return driver.execute_script(
            'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).getAttribute('
            '"src")',
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.INSTRUCTION_IMAGE_PART)

    def verify_qr_code_image_part_displayed(self, driver):
        return driver.execute_script(
            'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1])'
            '.firstElementChild.getAttribute("src")',
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.QR_CODE_PART)

    def verify_mobile_footer_content_part_displayed(self, driver):
        return driver.execute_script(
            self.script_textContent,
            SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.MOBILE_FOOTER_CONTENT_PART)

