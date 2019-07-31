from models.pageelements.settings import SettingsElements
from models.pagelocators.settings import SettingsPageLocators
from models.pageobject.basepage_object import BasePageObject


class SettingsPageObject(BasePageObject):
    settings_elem = SettingsElements()

    def click_continue_where_left_off_button(self, driver):
        element_continue_left_off = self.settings_elem.find_continue_where_left_off(driver)
        element_continue_left_off.click()

    def click_open_new_tab(self, driver):
        element_open_new_tab = self.settings_elem.find_open_new_tab(driver)
        element_open_new_tab.click()

    def click_open_a_specific_page(self, driver):
        element_open_a_specific_page = self.settings_elem.find_open_a_specific_set_of_pages(driver)
        element_open_a_specific_page.click()

    def click_add_a_new_page(self, driver):
        element_add_a_new_page = self.settings_elem.find_add_a_new_page(driver)
        element_add_a_new_page.click()

    def get_default_torrent_value(self, driver):
        default_torrent_value = self.settings_elem.find_default_torrent_client(driver)
        return default_torrent_value.text

    def get_max_connection_per_torrent_client_value(self, driver):
        max_connection = self.settings_elem.find_max_number_of_connection_per_client(driver)
        test1_executed = driver.execute_script('return arguments[0].shadowRoot', max_connection)
        return test1_executed.text

