from models.pageelements.extensions import ExtensionsElement, CocCocSaviorExtensionDetailElement, \
    SaviorExtensionsOptionsElement, GoogleExtensionsStorePageElements
from models.pageobject.basepage_object import BasePageObject
from utils_automation.setup import WaitAfterEach


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
                    print("Already enable ublock")
                else:
                    raise Exception
            elif action == 'disable':
                if ublock_toggle_elem.get_attribute('aria-pressed') == 'true':
                    ublock_knob_elem.click()
                elif ublock_toggle_elem.get_attribute('aria-pressed') == 'false':
                    print("Already disable ublock")
                else:
                    raise Exception
            else:
                raise Exception


class ExtensionsDetailsPageObject(BasePageObject):
    savior_extensions_details = CocCocSaviorExtensionDetailElement()
    extensions_element = ExtensionsElement()

    def savior_button_is_enabled(self, driver):
        savior_button_enabled_element = self.savior_extensions_details.find_coccoc_savior_enable_button(driver)
        assert savior_button_enabled_element.get_attribute('aria-disabled') == 'true'
        assert savior_button_enabled_element.get_attribute('aria-pressed') == 'true'

    def savior_incognito_is_disabled(self, driver):
        savior_incognito_element = self.savior_extensions_details.find_coccoc_savior_incognitor_checkbox_button(driver)
        assert savior_incognito_element.get_attribute('aria-disabled') == 'false'
        assert savior_incognito_element.get_attribute('aria-pressed') == 'false'

    def open_extension_options_view(self, driver):
        self.savior_extensions_details.find_extension_options_button(driver).click()

    def on_off_extension_in_detail_page(self, driver, is_on_extension=True):
        on_off_btn = self.extensions_element.find_extension_toggle_button(driver)
        on_off_btn_status = on_off_btn.get_attribute("aria-pressed")
        if is_on_extension:
            if on_off_btn_status in "false":
                on_off_btn.click()
        elif is_on_extension is False:
            if on_off_btn_status in "true":
                on_off_btn.click()


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

