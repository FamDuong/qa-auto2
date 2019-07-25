
import time

from models.pageobject.settings import SettingsPageObject


class TestInternalSettings:

    settings_page_object = SettingsPageObject()
    coccoc_setting_url = "coccoc://settings"

    def test_click_continue_where_left_off(self, browser):
        browser.get(self.coccoc_setting_url)
        time.sleep(3)
        self.settings_page_object.click_continue_where_left_off_button(browser)
        time.sleep(2)

    def test_click_open_with_new_tab(self, browser):
        browser.get(self.coccoc_setting_url)
        self.settings_page_object.click_open_new_tab(browser)
        time.sleep(2)

    def test_click_open_a_specific_set_of_pages(self, browser):
        browser.get(self.coccoc_setting_url)
        self.settings_page_object.click_open_a_specific_page(browser)
        self.settings_page_object.click_add_a_new_page(browser)
        # browser.switch_to_active_element()
        # browser.find_element_by_id("input").send_keys("http://kenh14.vn/")
        # browser.find_element_by_id("actionButton").click()
        # time.sleep(2)


