from models.pageelements.savior import SaviorElements
from models.pageobject.basepage_object import BasePageObject


class SaviorPageObject(BasePageObject):
    savior_elements = SaviorElements()

    def download_button_is_displayed(self, driver):
        self.savior_elements.find_download_button(driver)

    def not_found_download_button(self, driver):
        self.savior_elements.not_found_download_button(driver)
