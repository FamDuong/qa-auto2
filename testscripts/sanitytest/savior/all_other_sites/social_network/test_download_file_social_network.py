from pytest_testrail.plugin import pytestrail
from utils_automation.const import OtherSiteUrls


class TestFacebook:

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        browser.get(OtherSiteUrls.FACEBOOK_VIDEO_URL)




