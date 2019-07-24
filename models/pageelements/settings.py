from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.settings import SettingsPageLocators


class SettingsElements(BasePageElement):

    def find_continue_where_left_off(self, driver):
        return self.find_shadow_element(driver, SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_ON_START_UP_PAGE_TEXT,
                                        SettingsPageLocators.CONTINUE_WHERE_LEFT_OFF_TEXT)

    def find_open_new_tab(self, driver):
        return self.find_shadow_element(driver,SettingsPageLocators.SETTINGS_UI_TEXT,
                                        SettingsPageLocators.SETTINGS_MAIN_TEXT,
                                        SettingsPageLocators.SETTINGS_BASIC_PAGE_TEXT,
                                        SettingsPageLocators.SETTINGS_ON_START_UP_PAGE_TEXT,
                                        SettingsPageLocators.OPEN_NEW_TAB_PAGE_TEXT)
