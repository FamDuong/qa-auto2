from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.settings import SettingsPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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