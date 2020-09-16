from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail

from testscripts.common_setup import implement_download_file, \
    clear_data_download_in_browser_and_download_folder
from utils_automation.const import OtherSiteUrls

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()


class TestNhacVN:

    @pytestrail.case('C98782')
    def test_download_nhac_vn(self, browser, get_current_download_folder, clear_download_page):
        browser.get(OtherSiteUrls.NHAC_VN_VIDEO_URL)
        any_site_page_object.mouse_over_video_nhac_vn(browser)
        implement_download_file(browser, get_current_download_folder, ),
        clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)