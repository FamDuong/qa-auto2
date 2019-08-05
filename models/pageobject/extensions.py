import time

from models.pageelements.extensions import ExtensionsElement, CocCocSaviorExtensionDetailElement
from models.pagelocators.extensions import ExtensionsPageLocators
from models.pageobject.basepage_object import BasePageObject


class ExtensionsPageObject(BasePageObject):

    extension_elem = ExtensionsElement()

    def savior_extension_is_displayed(self, driver):
        assert self.extension_elem.find_savior_extension(driver).text == 'Cốc Cốc Savior'

    def savior_extension_detail_is_clicked(self, driver):
        savior_detail = self.extension_elem.find_savior_details(driver)
        savior_detail.click()


class ExtensionsDetailsPageObject(BasePageObject):
    extensions_details = CocCocSaviorExtensionDetailElement()

    def savior_button_is_enabled(self, driver):
        savior_button_enabled_element = self.extensions_details.find_coccoc_savior_enable_button(driver)
        assert savior_button_enabled_element.get_attribute('aria-disabled') == 'true'
        assert savior_button_enabled_element.get_attribute('aria-checked') == 'true'

    def savior_incognito_is_disabled(self, driver):
        savior_incognito_element = self.extensions_details.find_coccoc_savior_incognitor_checkbox_button(driver)
        assert savior_incognito_element.get_attribute('aria-disabled') == 'false'
        assert savior_incognito_element.get_attribute('aria-checked') == 'false'


