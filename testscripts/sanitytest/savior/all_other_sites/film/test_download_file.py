from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from utils_automation.const import OtherSiteUrls
from utils_automation.setup import WaitAfterEach

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()


class TestPhimmoi:

    @staticmethod
    def pause_video_element_phimmoi(browser):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        any_site_page_object.click_video_element_phimmoi(browser)
        any_site_page_object.mouse_over_video_element_phimmoi(browser)
        any_site_page_object.mouse_over_video_element_phimmoi(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        browser.get(OtherSiteUrls.PHIMMOI_VIDEO_URL)
        list_windows = browser.window_handles
        print(list_windows)
        browser.switch_to.window(list_windows[0])
        any_site_page_object.close_popup_continue_watching(browser)
        self.pause_video_element_phimmoi(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_check_click_download_button_default_quality(self, browser, get_current_download_folder):
        pass




