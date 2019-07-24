from models.pageelements.settings import SettingsElements
from models.pageobject.basepage_object import BasePageObject


class SettingsPageObject(BasePageObject):

    def click_continue_where_left_off_button(self, driver):
        element_continue_left_off = SettingsElements.find_continue_where_left_off(driver)
        element_continue_left_off.click()

