import time
from selenium import webdriver
from models.pageobject.settings import SettingsPageObject
from utils.const import Urls


class TestOnStartUp:

    settings_page_object = SettingsPageObject()

    def test_click_continue_where_left_off(self, browser):
        browser.get(Urls.COCCOC_SETTINGS_URL)
        self.settings_page_object.click_continue_where_left_off_button(browser)

    def test_click_open_with_new_tab(self, browser):
        browser.get(Urls.COCCOC_SETTINGS_URL)
        self.settings_page_object.click_open_new_tab(browser)

    def test_click_open_a_specific_set_of_pages(self, browser):
        browser.get(Urls.COCCOC_SETTINGS_URL)
        self.settings_page_object.click_open_a_specific_page(browser)
        self.settings_page_object.click_add_a_new_page(browser)
        # browser.switch_to_active_element()
        # browser.find_element_by_id("input").send_keys("http://kenh14.vn/")
        # browser.find_element_by_id("actionButton").click()
        # time.sleep(2)


