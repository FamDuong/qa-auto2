import pytz
from pytest_testrail.plugin import pytestrail

from models.pageobject.downloads import DownloadsPageObject
from models.pageobject.version import VersionPageObject


class TestBrowser:
    download_page_object = DownloadsPageObject()
    version_page_object = VersionPageObject()

    def select_shadow_element_by_css_selector(self, browser, selector):
        element = browser.execute_script('return arguments[0].shadowRoot', selector)
        return element

    @pytestrail.case('C36161')
    def test_current_time_now(self):
        assert True

    def test_timezone(self):
        print(pytz.all_timezones)
