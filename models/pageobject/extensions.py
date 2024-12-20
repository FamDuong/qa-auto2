import logging
import time
from datetime import datetime
from models.pageelements.extensions import ExtensionsElement, CocCocSaviorExtensionDetailElement, \
    SaviorExtensionsOptionsElement, GoogleExtensionsStorePageElements, ABPExtensionsDetailPageElements
from models.pagelocators.extensions import ExtensionsPageLocators
from models.pagelocators.settings import SettingsPageLocators
from models.pageobject.basepage_object import BasePageObject
import settings_master as settings
from models.pageobject.settings import SettingsPageObject
from utils_automation.setup import WaitAfterEach

LOGGER = logging.getLogger(__name__)


class ExtensionsPageObject(BasePageObject):
    extension_elem = ExtensionsElement()

    def savior_extension_is_displayed(self, driver):
        assert self.extension_elem.find_savior_extension(driver).text == 'Cốc Cốc Savior'

    def savior_extension_detail_is_clicked(self, driver):
        driver.execute_script('arguments[0].scrollIntoView()', self.extension_elem.find_savior_details(driver))
        WaitAfterEach.sleep_timer_after_each_step()
        self.extension_elem.find_savior_details(driver).click()

    def click_extension_detail_button(self, driver, extension_id):
        driver.execute_script('arguments[0].click()',
                              self.extension_elem.find_extension_detail_button(driver, extension_id))

    def get_attribute_toggle_button_in_detail_extension(self, driver, attribute_name):
        return driver.execute_script('return arguments[0].getAttribute(arguments[1])',
                                     self.extension_elem.find_extension_toggle_button(driver),
                                     attribute_name)

    class UblockPlusPageObject(BasePageObject):
        ublock_elem = ExtensionsElement.UblockPlusAdblockerElement()

        def interact_with_ublock_knob_btn(self, driver, action='enable'):
            ublock_toggle_elem = self.ublock_elem.find_ublock_toggle_btn(driver)
            ublock_knob_elem = self.ublock_elem.find_ublock_toggle_knob_btn(driver)
            if action == 'enable':
                if ublock_toggle_elem.get_attribute('aria-pressed') == 'false':
                    ublock_knob_elem.click()
                elif ublock_toggle_elem.get_attribute('aria-pressed') == 'true':
                    LOGGER.info("Already enable ublock")
                else:
                    raise Exception
            elif action == 'disable':
                if ublock_toggle_elem.get_attribute('aria-pressed') == 'true':
                    ublock_knob_elem.click()
                elif ublock_toggle_elem.get_attribute('aria-pressed') == 'false':
                    LOGGER.info("Already disable ublock")
                else:
                    raise Exception
            else:
                raise Exception


class ExtensionsDetailsPageObject(BasePageObject):
    extensions_details = CocCocSaviorExtensionDetailElement()
    extensions_page_object = ExtensionsPageObject()

    def savior_button_is_enabled(self, driver):
        savior_button_enabled_element = self.extensions_details.find_coccoc_savior_enable_button(driver)
        assert savior_button_enabled_element.get_attribute('aria-disabled') == 'true'
        assert savior_button_enabled_element.get_attribute('aria-pressed') == 'true'

    def savior_incognito_is_disabled(self, driver):
        savior_incognito_element = self.extensions_details.find_coccoc_savior_incognitor_checkbox_button(driver)
        assert savior_incognito_element.get_attribute('aria-disabled') == 'false'
        assert savior_incognito_element.get_attribute('aria-pressed') == 'false'

    def open_extension_options_view(self, driver):
        self.extensions_details.find_extension_options_button(driver).click()

    def click_coc_coc_ad_block_extension_details_button(self, driver):
        self.extensions_page_object.click_extension_detail_button(driver, ExtensionsPageLocators.COCCOC_ADBLOCK_ID)


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
        WaitAfterEach.sleep_timer_after_each_step()

    def verify_return_value_show_instant_download_youtube(self, driver):
        return self.savior_extension.find_instant_download_youtube_option(driver).get_attribute('checked')

    def choose_save_and_close_button(self, driver):
        self.savior_extension.find_save_and_close_button(driver).click()
        WaitAfterEach.sleep_timer_after_each_step()

    def verify_show_download_button_near_is_checked(self, driver):
        element_checked = self.savior_extension.find_show_download_button_near_downloadable_media(driver)
        return element_checked.get_attribute('checked')

    def click_show_download_button_near(self, driver):
        self.savior_extension.find_show_download_button_near_downloadable_media(driver).click()

    def choose_video_quality_high(self, driver):
        self.savior_extension.find_video_quality_high_option(driver).click()

    def choose_video_quality_low(self, driver):
        self.savior_extension.find_video_quality_low_option(driver).click()

    def choose_video_quality_medium(self, driver):
        self.savior_extension.find_video_quality_medium_option(driver).click()

    def verify_video_quality_medium_is_checked(self, driver):
        return self.savior_extension.find_video_quality_medium_option(driver).get_attribute('checked')

    def verify_video_quality_high_is_checked(self, driver):
        return self.savior_extension.find_video_quality_high_option(driver).get_attribute('checked')

    def choose_remember_last_chosen_option(self, driver):
        remember_option_element = self.savior_extension.find_remember_last_chosen_option(driver)
        checked_value = remember_option_element.get_attribute('checked')
        self.checked_value_condition(checked_value, remember_option_element)


class GoogleExtensionsStorePageObject(BasePageObject):
    google_extensions_store_elem = GoogleExtensionsStorePageElements()

    def get_rung_rinh_extension_version(self, driver):
        return self.google_extensions_store_elem.find_rung_rinh_extension_version(driver).text


class ABPExtensionsDetailPageObject(BasePageObject):
    abp_extension_elem = ABPExtensionsDetailPageElements()
    setting_page_obj = SettingsPageObject()
    LOGGER = logging.getLogger(__name__)

    def click_extension_options(self, driver):
        extension_options_icon = self.abp_extension_elem.find_extension_options(driver)
        driver.execute_script('arguments[0].click()', extension_options_icon)

    def select_abp_mode(self, driver, visible_text):
        self.abp_extension_elem.switch_to_change_mode_iframe(driver)
        self.abp_extension_elem.select_mode_dropdownlist(driver, visible_text)

    def wait_until_finish_update_abp_to_latest(self, driver):
        driver.maximize_window()
        self.setting_page_obj.open_coc_coc_extension_page(driver)
        self.LOGGER.info("Update extension")
        actual_abp_version = self.setting_page_obj.get_extension_version(driver, SettingsPageLocators.EXTENSION_AD_BLOCK_PLUS)
        expect_adp_version = settings.EXTENSION_VERSION_AD_BLOCK_PLUS
        self.LOGGER.info("Actual Extension: "+actual_abp_version)
        self.LOGGER.info("Expect Extension: "+expect_adp_version)
        start_time = datetime.now()
        if actual_abp_version not in expect_adp_version:
            while actual_abp_version not in expect_adp_version:
                self.setting_page_obj.update_extension(driver)
                time.sleep(2)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 30:
                    break

