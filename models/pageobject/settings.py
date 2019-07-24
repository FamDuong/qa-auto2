from models.pageelements.settings import SettingsElements
from models.pageobject.basepage_object import BasePageObject


class SettingsPageObject(BasePageObject):
    settings_elem = SettingsElements()

    def click_continue_where_left_off_button(self, driver):
        element_continue_left_off = self.settings_elem.find_continue_where_left_off(driver)
        element_continue_left_off.click()

    def click_open_new_tab(self, driver):
        element_open_new_tab = self.settings_elem.find_open_new_tab(driver)
        element_open_new_tab.click()

