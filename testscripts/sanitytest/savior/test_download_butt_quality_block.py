from models.pageobject.extensions import SaviorExtensionOptionsPageObject
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import YoutubePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import pause_any_video_youtube


class TestDownloadButtQualityBlock:
    youtube_page_object = YoutubePageObject()
    savior_page_object = SaviorPageObject()

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        pause_any_video_youtube(browser, self.youtube_page_object)
        self.savior_page_object.assert_value_preferred_quality(browser, 'High')
