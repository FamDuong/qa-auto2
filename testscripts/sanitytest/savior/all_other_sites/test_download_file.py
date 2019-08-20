from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from utils_automation.const import OtherSiteUrls


any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()


class Test24H:

    @staticmethod
    def pause_video_element_24h(browser):
        browser.get(OtherSiteUrls.TWENTY_FOUR_H_VIDEO_URL)
        any_site_page_object.click_video_element_24h(browser)
        any_site_page_object.mouse_over_video_element_24h(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.pause_video_element_24h(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')


