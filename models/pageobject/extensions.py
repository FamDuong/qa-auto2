import time

from models.pageelements.extensions import ExtensionsElement, CocCocSaviorExtensionDetailElement, \
    SaviorExtensionsOptionsElement
from models.pagelocators.extensions import ExtensionsPageLocators
from models.pageobject.basepage_object import BasePageObject


class ExtensionsPageObject(BasePageObject):

    extension_elem = ExtensionsElement()

    def savior_extension_is_displayed(self, driver):
        assert self.extension_elem.find_savior_extension(driver).text == 'Cốc Cốc Savior'

    def savior_extension_detail_is_clicked(self, driver):
        self.extension_elem.find_savior_details(driver).click()


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

    def open_extension_options_view(self, driver):
        self.extensions_details.find_extension_options_button(driver).click()


class SaviorExtensionOptionsPageObject(BasePageObject):
    savior_extension = SaviorExtensionsOptionsElement()

    def checked_value_condition(self, checked_value, element):
        if checked_value is None:
            element.click()
        else:
            return 0

    def get_show_instant_download_youtube_value(self, driver):
        show_instant_download_youtube = self.savior_extension.find_extensions_wrapper(driver)
        return show_instant_download_youtube.get_attribute('extension')

    def choose_show_instant_download_youtube(self, driver):
        show_instant = self.savior_extension.find_instant_download_youtube_option(driver)
        checked_value = show_instant.get_attribute('checked')
        self.checked_value_condition(checked_value, show_instant)
        time.sleep(1)

    def verify_return_value_show_instant_download_youtube(self, driver):
        return self.savior_extension.find_instant_download_youtube_option(driver).get_attribute('checked')

    def choose_save_and_close_button(self, driver):
        self.savior_extension.find_save_and_close_button(driver).click()
        time.sleep(1)

    def verify_show_download_button_near_is_checked(self, driver):
        element_checked = self.savior_extension.find_show_download_button_near_downloadable_media(driver)
        return element_checked.get_attribute('checked')

    def click_show_download_button_near(self, driver):
        self.savior_extension.find_show_download_button_near_downloadable_media(driver).click()

    def choose_video_quality_high(self, driver):
        self.savior_extension.find_video_quality_high_option(driver).click()

    def verify_video_quality_medium_is_checked(self, driver):
        return self.savior_extension.find_video_quality_medium_option(driver).get_attribute('checked')

    def verify_video_quality_high_is_checked(self, driver):
        return self.savior_extension.find_video_quality_high_option(driver).get_attribute('checked')

    def choose_remember_last_chosen_option(self, driver):
        remember_option_element = self.savior_extension.find_remember_last_chosen_option(driver)
        checked_value = remember_option_element.get_attribute('checked')
        self.checked_value_condition(checked_value, remember_option_element)




