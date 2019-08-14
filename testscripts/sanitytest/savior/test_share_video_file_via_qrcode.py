import time

from models.pageobject.savior import SaviorPageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import pause_any_video_youtube


class TestShareVideoFileQRCode:
    savior_page_object = SaviorPageObject()

    @pytestrail.case('C54157')
    def test_check_default_state_of_mobile(self, browser):
        pause_any_video_youtube(browser)
        assert 'Mobile' in self.savior_page_object.verify_mobile_sharing_button_displayed(browser)

    @pytestrail.case('C54158')
    def test_check_layout_of_send_to_mobile(self, browser):
        pause_any_video_youtube(browser)
        self.savior_page_object.choose_mobile_sharing_button(browser)
        assert 'savior-mobile-download.gif' in self.savior_page_object.verify_instruction_image_part_displayed(browser)
        assert 'data:image/png;base64' in self.savior_page_object.verify_qr_code_image_part_displayed(browser)
        assert 'Browser on mobile?' in self.savior_page_object.verify_mobile_footer_content_part_displayed(browser)

    @pytestrail.case('C54159')
    def test_check_switcher_shared_file_format(self, browser):
        pause_any_video_youtube(browser)
        self.savior_page_object.choose_mobile_sharing_button(browser)
        assert '' == self.savior_page_object.verify_if_video_is_focused(browser)

