import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.extensions import ExtensionsPageLocators, SaviorDetailsPageLocators, \
    SaviorExtensionOptionsPageLocators
from utils_automation.setup import WaitAfterEach


class ExtensionsElement(BasePageElement):

    def find_list_extensions(self, driver):
        return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                        ExtensionsPageLocators.EXTENSIONS_ITEM_LIST,
                                        ExtensionsPageLocators.EXTENSIONS_ITEM_CONTAINER_CSS)

    def find_savior_extension_wrapper(self, driver):
        list_elements = self.find_list_extensions(driver)
        WaitAfterEach.sleep_timer_after_each_step()

        savior_wrapper = list_elements.find_element_by_id(ExtensionsPageLocators.SAVIOR_EXTENSIONS_WRAPPER_ID)
        WaitAfterEach.sleep_timer_after_each_step()

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

    def find_extension_options_button(self, driver):
        return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                        SaviorDetailsPageLocators.EXTENSION_DETAIL_VIEW,
                                        SaviorDetailsPageLocators.CR_LINK_ROW,
                                        SaviorDetailsPageLocators.CR_ICON_BUTTON,
                                        SaviorDetailsPageLocators.EXTENSION_OPTIONS_ICON)


class SaviorExtensionsOptionsElement(BasePageElement):

    def find_extensions_wrapper(self, driver):
        return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                 SaviorDetailsPageLocators.EXTENSION_OPTIONS_DIALOG,
                                 SaviorDetailsPageLocators.EXTENSION_OPTIONS)

    def find_instant_download_youtube_option(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(SaviorExtensionOptionsPageLocators.SHOW_INSTANT_DOWNLOAD_YOUTUBE))

    def find_save_and_close_button(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(SaviorExtensionOptionsPageLocators.SAVE_AND_CLOSE_BTN))

    def find_show_download_button_near_downloadable_media(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(SaviorExtensionOptionsPageLocators.SHOW_DOWNLOAD_BTN_NEAR_DOWNLOAD_MEDIA))

    def find_video_quality_high_option(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(SaviorExtensionOptionsPageLocators.VIDEO_QUALITY_HIGH_BTN))

    def find_video_quality_low_option(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(SaviorExtensionOptionsPageLocators.VIDEO_QUALITY_LOW_BTN))

    def find_video_quality_medium_option(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(SaviorExtensionOptionsPageLocators.VIDEO_QUALITY_MEDIUM_BTN))

    def find_remember_last_chosen_option(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(SaviorExtensionOptionsPageLocators.REMEMBER_LAST_CHOSEN_OPTION))






