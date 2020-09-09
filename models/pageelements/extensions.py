from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.extensions import ExtensionsPageLocators, SaviorDetailsPageLocators, \
    SaviorExtensionOptionsPageLocators, GoogleExtensionsStorePageLocators, UblockPlusPageLocators, \
    AdBlockPlusDetailsPageLocators
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
        return self.find_savior_extension_wrapper(driver).find_element_by_id(
            ExtensionsPageLocators.EXTENSION_DETAIL_BUTTON)

    def find_extension_detail_button(self, driver, extension_id):
        return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                        ExtensionsPageLocators.ITEMS_LIST, extension_id,
                                        ExtensionsPageLocators.EXTENSION_DETAIL_BUTTON_ID)

    def find_extension_toggle_button(self, driver):
        return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                        ExtensionsPageLocators.EXTENSION_DETAIL_VIEW,
                                        ExtensionsPageLocators.EXTENSION_TOGGLE_BUTTON)

    class UblockPlusAdblockerElement(BasePageElement):

        def find_ublock_toggle_knob_btn(self, driver):
            return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT
                                            , ExtensionsPageLocators.EXTENSIONS_ITEM_LIST
                                            , UblockPlusPageLocators.UBLOCK_PLUS_ID_CSS_LOCATOR
                                            , UblockPlusPageLocators.ENABLE_TOGGER_BTN
                                            , UblockPlusPageLocators.KNOB_BTN)

        def find_ublock_toggle_btn(self, driver):
            return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT
                                            , ExtensionsPageLocators.EXTENSIONS_ITEM_LIST
                                            , UblockPlusPageLocators.UBLOCK_PLUS_ID_CSS_LOCATOR
                                            , UblockPlusPageLocators.ENABLE_TOGGER_BTN)


class CocCocSaviorExtensionDetailElement(BasePageElement):
    def find_coccoc_savior_enable_button(self, driver):
        return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                        SaviorDetailsPageLocators.EXTENSION_DETAIL_VIEW,
                                        SaviorDetailsPageLocators.SAVIOR_ENABLE_BUTTON_CSS)

    def find_coccoc_savior_incognitor_checkbox_button(self, driver):
        return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                        SaviorDetailsPageLocators.EXTENSION_DETAIL_VIEW,
                                        SaviorDetailsPageLocators.EXTENSION_TOGGLE_ROW,
                                        SaviorDetailsPageLocators.SAVIOR_INCOGNITO_ENABLE_BUTTON_CSS)

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
        instant_download_youtube_option = self.find_element_if_exist(driver, SaviorExtensionOptionsPageLocators.SHOW_INSTANT_DOWNLOAD_YOUTUBE)
        return instant_download_youtube_option

    def find_save_and_close_button(self, driver):
        save_and_close_button = self.find_element_if_exist(driver, SaviorExtensionOptionsPageLocators.SAVE_AND_CLOSE_BTN)
        return save_and_close_button

    def find_show_download_button_near_downloadable_media(self, driver):
        show_download_button_near_downloadable_media = self.find_element_if_exist(driver, SaviorExtensionOptionsPageLocators.SHOW_DOWNLOAD_BTN_NEAR_DOWNLOAD_MEDIA)
        return show_download_button_near_downloadable_media

    def find_video_quality_high_option(self, driver):
        video_quality_high_option = self.find_element_if_exist(driver, SaviorExtensionOptionsPageLocators.VIDEO_QUALITY_HIGH_BTN)
        return video_quality_high_option

    def find_video_quality_low_option(self, driver):
        video_quality_low_option = self.find_element_if_exist(driver, SaviorExtensionOptionsPageLocators.VIDEO_QUALITY_LOW_BTN)
        return video_quality_low_option

    def find_video_quality_medium_option(self, driver):
        video_quality_medium_option = self.find_element_if_exist(driver, SaviorExtensionOptionsPageLocators.VIDEO_QUALITY_MEDIUM_BTN)
        return video_quality_medium_option

    def find_remember_last_chosen_option(self, driver):
        remember_last_chosen_option = self.find_element_if_exist(driver, SaviorExtensionOptionsPageLocators.REMEMBER_LAST_CHOSEN_OPTION)
        return remember_last_chosen_option


class GoogleExtensionsStorePageElements(BasePageElement):

    def find_rung_rinh_extension_version(self, driver):
        rung_rinh_extension_version = self.find_element_if_exist(driver, GoogleExtensionsStorePageLocators.RUNG_RINH_EXTENSION_VERSION)
        return rung_rinh_extension_version


class ABPExtensionsDetailPageElements(BasePageElement):

    def find_extension_options(self, driver):
        return self.find_shadow_element(driver, ExtensionsPageLocators.EXTENSIONS_MANAGER_TEXT,
                                        ExtensionsPageLocators.EXTENSION_DETAIL_VIEW,
                                        AdBlockPlusDetailsPageLocators.EXTENSION_OPTIONS,
                                        AdBlockPlusDetailsPageLocators.EXTENSION_OPTIONS_ICON_PARENT,
                                        AdBlockPlusDetailsPageLocators.EXTENSION_OPTIONS_ICON)

    def switch_to_change_mode_iframe(self, driver):
        change_mode_iframe = self.find_element_if_exist(driver, AdBlockPlusDetailsPageLocators.CHANGE_MODE_IFRAME)
        driver.switch_to.frame(change_mode_iframe)

    def select_mode_dropdownlist(self, driver, visible_text):
        from selenium.webdriver.support.ui import Select
        element_ddl = Select(self.find_element_if_exist(driver, AdBlockPlusDetailsPageLocators.SELECT_MODE_DDL))
        element_ddl.select_by_visible_text(visible_text)

