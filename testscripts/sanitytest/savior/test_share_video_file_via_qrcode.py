from models.pageobject.savior import SaviorPageObject
from pytest_testrail.plugin import pytestrail
from testscripts.common_setup import pause_any_video_youtube


class TestShareVideoFileQRCode:
    savior_page_object = SaviorPageObject()

    def open_mobile_sharing_pop_up(self, browser):
        pause_any_video_youtube(browser)
        self.savior_page_object.choose_mobile_sharing_button(browser)

    def handle_store_button(self, browser, text_assert):
        list_windows = browser.window_handles
        if len(list_windows) == 2:
            browser.switch_to.window(list_windows[1])
        elif len(list_windows) == 3:
            browser.switch_to.window(list_windows[2])
        assert text_assert in browser.current_url
        browser.close()
        browser.switch_to.window(list_windows[0])

    @pytestrail.case('C54157')
    def test_check_default_state_of_mobile(self, browser):
        pause_any_video_youtube(browser)
        assert 'Mobile' in self.savior_page_object.verify_mobile_sharing_button_displayed(browser)

    @pytestrail.case('C54158')
    def test_check_layout_of_send_to_mobile(self, browser):
        self.open_mobile_sharing_pop_up(browser)
        assert 'savior-mobile-download.gif' in self.savior_page_object.verify_instruction_image_part_displayed(browser)
        assert 'data:image/png;base64' in self.savior_page_object.verify_qr_code_image_part_displayed(browser)
        assert 'Browser on mobile?' in self.savior_page_object.verify_mobile_footer_content_part_displayed(browser)

    @pytestrail.case('C54159')
    def test_check_switcher_shared_file_format(self, browser):
        self.open_mobile_sharing_pop_up(browser)
        assert '' == self.savior_page_object.verify_if_video_is_focused(browser)

    @pytestrail.case('C54160')
    def test_check_the_download_link_on_mobile_popup(self, browser):
        self.open_mobile_sharing_pop_up(browser)
        self.savior_page_object.choose_google_play_button(browser)
        # Assert for google play button
        self.handle_store_button(browser, 'com.coccoc')
        self.savior_page_object.choose_app_store_button(browser)
        # Assert for google play button
        self.handle_store_button(browser, 'browser')






