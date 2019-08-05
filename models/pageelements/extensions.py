import time

from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.extensions import ExtensionsPageLocators, SaviorDetailsPageLocators


class ExtensionsElement(BasePageElement):

    def find_list_extensions(self, driver):
        return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                        ExtensionsPageLocators.EXTENSIONS_ITEM_LIST,
                                        ExtensionsPageLocators.EXTENSIONS_ITEM_CONTAINER_CSS)

    def find_savior_extension_wrapper(self, driver):
        list_elements = self.find_list_extensions(driver)
        time.sleep(2)
        savior_wrapper = list_elements.find_element_by_id(ExtensionsPageLocators.SAVIOR_EXTENSIONS_WRAPPER_ID)
        time.sleep(1)
        return self.select_shadow_element_by_css_selector(driver, savior_wrapper)

    def find_savior_extension(self, driver):
        return self.find_savior_extension_wrapper(driver).find_element_by_id('name')

    def find_savior_details(self, driver):
        return self.find_savior_extension_wrapper(driver).find_element_by_id(ExtensionsPageLocators.EXTENSION_DETAIL_BUTTON)


class CocCocSaviorExtensionDetailElement(BasePageElement):
    def find_coccoc_savior_enable_button(self, driver):
        return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                        SaviorDetailsPageLocators.EXTENSION_DETAIL_VIEW,
                                        SaviorDetailsPageLocators.EXTENSION_DETAIL_CR_CHECKBOX,
                                        SaviorDetailsPageLocators.SAVIOR_ENABLE_BUTTON_CSS)

    def find_coccoc_savior_incognitor_checkbox_button(self, driver):
        return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                        SaviorDetailsPageLocators.EXTENSION_DETAIL_VIEW,
                                        SaviorDetailsPageLocators.EXTENSION_TOGGLE_ROW,
                                        SaviorDetailsPageLocators.EXTENSION_DETAIL_CR_CHECKBOX,
                                        SaviorDetailsPageLocators.SAVIOR_ENABLE_BUTTON_CSS)




