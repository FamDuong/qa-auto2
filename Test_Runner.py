from models.pageobject.downloads import DownloadsPageObject
from models.pageobject.version import VersionPageObject
from utils.const import Urls
from selenium import webdriver


class TestBrowser:
    download_page_object = DownloadsPageObject()
    version_page_object = VersionPageObject()

    def select_shadow_element_by_css_selector(self, browser, selector):
        element = browser.execute_script('return arguments[0].shadowRoot', selector)
        return element

    def test_current_time_now(self, browser):
        browser.get(Urls.COCCOC_DOWNLOAD_URL)
        self.download_page_object.cancel_all_current_torrent(browser)
        self.download_page_object.clear_all_existed_torrent(browser)

    def test_get_profile_path(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Urls.COCCOC_VERSION_URL)
        full_path_value = self.version_page_object.get_profile_path(driver)
        print(full_path_value)

