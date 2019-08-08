
from pytest_testrail.plugin import pytestrail
from models.pageobject.settings import SettingsPageObject
from utils_automation.const import Urls


# driver = None
#
# @pytest.fixture()
# def browser_local():
#     global driver
#     driver = webdriver.Chrome()
#     return driver


class TestOnStartUp:

    settings_page_object = SettingsPageObject()

    # def open_close(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("coccoc://settings")
    #     time.sleep(2)
    #     self.settings_page_object.click_continue_where_left_off_button(self.driver)
    #     time.sleep(2)
    #     self.driver.close()
    #
    #     self.another_driver = webdriver.Chrome()

    @pytestrail.case('C43219')
    def test_click_continue_where_left_off(self, browser):
        browser.get(Urls.COCCOC_SETTINGS_URL)
        self.settings_page_object.click_continue_where_left_off_button(browser)

    @pytestrail.case('C43218')
    def test_click_open_with_new_tab(self, browser):
        browser.get(Urls.COCCOC_SETTINGS_URL)
        self.settings_page_object.click_open_new_tab(browser)

    @pytestrail.case('C43220')
    def test_click_open_a_specific_set_of_pages(self, browser):
        browser.get(Urls.COCCOC_SETTINGS_URL)
        self.settings_page_object.click_open_a_specific_page(browser)
        self.settings_page_object.click_add_a_new_page(browser)
