from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.settings import SettingsPageLocators, SettingsComponentsPageLocators, \
    SettingsClearBrowserDataLocators, SettingsDarkmodeLocators


class SettingsElements(BasePageElement):

    def find_continue_where_left_off(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_ON_START_UP_PAGE_TEXT,
                                        SettingsPageLocators.CONTINUE_WHERE_LEFT_OFF_TEXT)

    def find_open_new_tab(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_ON_START_UP_PAGE_TEXT,
                                        SettingsPageLocators.OPEN_NEW_TAB_PAGE_TEXT)

    def find_open_a_specific_set_of_pages(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_ON_START_UP_PAGE_TEXT,
                                        SettingsPageLocators.OPEN_SPECIFIC_PAGE_OR_SET_OF_PAGES_TEXT)

    def find_add_a_new_page(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_ON_START_UP_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_START_UP_URLS_PAGE_TEXT,
                                        SettingsPageLocators.ADD_A_NEW_PAGE_TEXT)

    def find_default_torrent_client(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_DEFAULT_BROWSER_PAGE_TEXT,
                                        SettingsPageLocators.DEFAULT_TORRENT_CLIENT_TEXT)

    def find_max_number_of_connection_per_client(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_COCCOC_SECTION_PAGE_TEXT)

    def find_download_location_element(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_DOWNLOAD_PAGE_TEXT,
                                        SettingsPageLocators.DEFAULT_DOWNLOAD_PATH_TEXT)

    def find_run_automatically_on_system_startup(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_DEFAULT_BROWSER_PAGE_TEXT,
                                        SettingsPageLocators.DEFAULT_BROWSER_RUN_AUTO_ONSTARTUP)

    def find_extension_version_by_id(self, driver, ext_id):
        return self.find_shadow_element(driver, SettingsPageLocators.EXTENSION_MAIN,
                                        SettingsPageLocators.EXTENSION_LIST,
                                        ext_id, SettingsPageLocators.EXTENSION_VERSION)

    def find_extension_on_off_by_id(self, driver, ext_id):
        return self.find_shadow_element(driver, SettingsPageLocators.EXTENSION_MAIN,
                                        SettingsPageLocators.EXTENSION_LIST,
                                        ext_id, SettingsPageLocators.EXTENSION_TOGGLE)

    def find_extension_toggle_developer_mode(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.EXTENSION_MAIN,
                                        SettingsPageLocators.EXTENSION_TOOLBAR,
                                        SettingsPageLocators.EXTENSION_TOGGLE_DEV_MODE)

    def find_extension_update_button(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.EXTENSION_MAIN,
                                        SettingsPageLocators.EXTENSION_TOOLBAR,
                                        SettingsPageLocators.EXTENSION_BTN_UPDATE)

    def find_extension_update_popup(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.EXTENSION_MAIN,
                                        SettingsPageLocators.EXTENSION_NOTIFY_PARENT,
                                        SettingsPageLocators.EXTENSION_NOTIFY)

    def wait_until_cc_version_update(self, driver):
        element = self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                           SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                           SettingsPageLocators.SETTINGS_ABOUT_TEXT,
                                           SettingsPageLocators.ABOUT_MESSAGE)
        self.text_to_be_present_in_shadow_element(element, "Cốc Cốc isdfsds up to date. dsdf")

    def find_default_browser_element(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_DEFAULT_BROWSER_PAGE_TEXT,
                                        "#isDefault")

    def find_make_default_browser_element(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_DEFAULT_BROWSER_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_DEFAULT_BROWSER_SECONDARY_TEXT)

    def find_coccoc_is_default_browser_element(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_DEFAULT_BROWSER_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_DEFAULT_BROWSER_IS_DEFAULT_TEXT)

    def find_make_default_browser_button(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_DEFAULT_BROWSER_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_DEFAULT_BROWSER_BUTTON_TEXT)

    def find_run_automatically_on_system_start_up_toggle(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_DEFAULT_BROWSER_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_TOGGLE_BUTTON_TEXT,
                                        SettingsPageLocators.SETTINGS_SYSTEM_START_UP_CONTROL_TEXT
                                        )

    def find_left_menu_people(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MENU_TEXT,
                                        SettingsPageLocators.SETTINGS_MENU_PEOPLE_LBL)

    def find_left_menu_auto_fill(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MENU_TEXT,
                                        SettingsPageLocators.SETTINGS_MENU_AUTO_FILL_LBL)

    def find_left_menu_default_browser(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MENU_TEXT,
                                        SettingsPageLocators.SETTINGS_MENU_DEFAULT_BROWSER_LBL)

    def find_relaunch_browser_btn(self, driver):
        index = 0
        from datetime import datetime
        start_time = datetime.now()
        while index == 0:
            try:
                element = self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                                   SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                                   SettingsPageLocators.SETTINGS_ABOUT_TEXT,
                                                   SettingsPageLocators.SETTINGS_ABOUT_RELAUNCH_BROWSER_TEXT)
                hidden_attribute = driver.execute_script("return arguments[0].hasAttribute('hidden')", element)
                if hidden_attribute is False:
                    index += 1
                    return element
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 120:
                    break
            except:
                import time
                time.sleep(2)

    def find_item_container_list_extensions(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.EXTENSION_MAIN,
                                        SettingsPageLocators.EXTENSIONS_ITEM_LIST,
                                        SettingsPageLocators.EXTENSIONS_CONTENT_WRAPPER)

    class SettingsAdsBlock(BasePageElement):

        def find_current_block_mod(self, driver):
            return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                            SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                            SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                            SettingsPageLocators.SettingsAdsBlockPageLocators
                                            .SUB_RESOURCE_FILTER_PAGE,
                                            SettingsPageLocators.SettingsAdsBlockPageLocators
                                            .CURRENT_BLOCK_MOD)

        def find_drop_down_menu_coccoc_block_ads(self, driver):
            return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                            SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                            SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                            SettingsPageLocators.SettingsAdsBlockPageLocators.SUB_RESOURCE_FILTER_PAGE,
                                            SettingsPageLocators.SettingsAdsBlockPageLocators.SETTINGS_DROP_DOWN_MENU,
                                            SettingsPageLocators.SettingsAdsBlockPageLocators.DROP_DOWN_MENU)


class SettingsComponentsPageElement(BasePageElement):

    def find_all_check_for_update_button(self, driver):
        return driver.find_elements_by_xpath(SettingsComponentsPageLocators.CHECK_FOR_UPDATE_BUTTON)

    def find_all_components_version(self, driver):
        return driver.find_elements_by_xpath(SettingsComponentsPageLocators.COMPONENT_VERSION_ELEMENT)


class SettingsClearBrowserDataPageElement(BasePageElement):
    def find_time_range_dropdown(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_MAIN,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_PRIVACY_PAGE,
                                        SettingsClearBrowserDataLocators.SETTINGS_CLEAR_BROWSING_DATA_DIALOG,
                                        SettingsClearBrowserDataLocators.SETTINGS_CLEAR_FROM_BASIC,
                                        SettingsClearBrowserDataLocators.SETTINGS_TIME_RANGE_DROPDOWN_MENU)

    def find_browsing_history_checkbox(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_MAIN,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_PRIVACY_PAGE,
                                        SettingsClearBrowserDataLocators.SETTINGS_CLEAR_BROWSING_DATA_DIALOG,
                                        SettingsClearBrowserDataLocators.SETTINGS_BROWSING_HISTORY_CHECKBOX_BASIC,
                                        SettingsClearBrowserDataLocators.SETTINGS_BROWSING_CHECKBOX,
                                        SettingsClearBrowserDataLocators.SETTINGS_BROWSING_CHILD_CHECKBOX)

    def find_cookies_and_other_site_data_checkbox(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_MAIN,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_PRIVACY_PAGE,
                                        SettingsClearBrowserDataLocators.SETTINGS_CLEAR_BROWSING_DATA_DIALOG,
                                        SettingsClearBrowserDataLocators.SETTINGS_BROWSING_COOKIES_CHECKBOX_BASIC,
                                        SettingsClearBrowserDataLocators.SETTINGS_BROWSING_CHECKBOX,
                                        SettingsClearBrowserDataLocators.SETTINGS_BROWSING_CHILD_CHECKBOX)

    def find_cached_images_and_files_checkbox(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_MAIN,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_PRIVACY_PAGE,
                                        SettingsClearBrowserDataLocators.SETTINGS_CLEAR_BROWSING_DATA_DIALOG,
                                        SettingsClearBrowserDataLocators.SETTINGS_BROWSING_CACHED_CHECKBOX_BASIC,
                                        SettingsClearBrowserDataLocators.SETTINGS_BROWSING_CHECKBOX,
                                        SettingsClearBrowserDataLocators.SETTINGS_BROWSING_CHILD_CHECKBOX)

    def find_clear_data_button(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_MAIN,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_PRIVACY_PAGE,
                                        SettingsClearBrowserDataLocators.SETTINGS_CLEAR_BROWSING_DATA_DIALOG,
                                        SettingsClearBrowserDataLocators.SETTINGS_CLEAR_DATA_BUTTON)


class SettingDarkmodePageElement(BasePageElement):
    # def find_alway_enable_dark_mode_element(self, driver):
    #     return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_COCCOC_SECTION_PAGE_TEXT,
    #                                     SettingsClearBrowserDataLocators.SETTINGS_PRIVACY_PAGE,
    #                                     SettingsDarkmodeLocators.SETTINGS_ANIMATED_PAGE,
    #                                     SettingsDarkmodeLocators.SETTINGS_SUB_PAGE,
    #                                     SettingsDarkmodeLocators.SETTINGS_CATEGORY_DEFAULT_SETTING,
    #                                     SettingsDarkmodeLocators.SETTINGS_CONTROLLED_RADIO_BUTTON,
    #                                     SettingsDarkmodeLocators.SETTINGS_DARKMODE_LABEL)

    def find_dark_mode_icon_for_site(self, driver):
        return driver.find_elements_by_xpath(SettingsDarkmodeLocators.SETTINGS_DARKMODE_ICON_FOR_SITE)
    #
    # def find_dark_mode_rules_button(self, driver):
    #     return driver.find_elements_by_xpath(SettingsDarkmodeLocators.COMPONENT_DARKMODE_BUTTON)

    def find_dark_mode_blocked_on_off_element(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_MAIN,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsDarkmodeLocators.SETTINGS_COCCOC_DARK_MODE_PAGE,
                                        SettingsPageLocators.SETTINGS_TOGGLE_BUTTON_TEXT,
                                        SettingsPageLocators.SETTINGS_SYSTEM_START_UP_CONTROL_TEXT)

    def find_dark_mode_always_enable_dark_mode_radio_box(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsClearBrowserDataLocators.SETTINGS_MAIN,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsDarkmodeLocators.SETTINGS_COCCOC_DARK_MODE_PAGE,
                                        SettingsDarkmodeLocators.SETTINGS_DARK_MODE_CONTROLLED_RADIO_BUTTON1,
                                        SettingsDarkmodeLocators.SETTINGS_DARK_MODE_RADIO_BOX)
