
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import implement_download_file, \
    clear_data_download_in_browser_and_download_folder, pause_any_video_site
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

    def prepare_displayed_savior_popup(self, browser):
        browser.get(OtherSiteUrls.PHIMMOI_VIDEO_URL)
        WaitAfterEach.sleep_timer_after_each_step()
        list_windows = browser.window_handles
        if len(list_windows) >= 2:
            browser.switch_to.window(list_windows[0])
            any_site_page_object.close_popup_continue_watching(browser)
        else:
            any_site_page_object.close_popup_continue_watching(browser)
        self.pause_video_element_phimmoi(browser)

    @pytestrail.case('C96721')
    def test_check_default_option(self, browser):
        self.prepare_displayed_savior_popup(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')


class TestVuViPhim:

    @staticmethod
    def prepare_savior_option_displayed(browser):
        browser.get(OtherSiteUrls.VU_VI_PHIM_VIDEO_URL)
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        any_site_page_object.double_click_video_item_vu_vi_phim(browser)
        browser.minimize_window()
        browser.maximize_window()
        any_site_page_object.mouse_over_video_item_vu_vi_phim(browser)
        WaitAfterEach.sleep_timer_after_each_step_longer_load()

    @pytestrail.case('C98751')
    def test_download_file_vuviphim(self, browser, get_current_download_folder):
        self.prepare_savior_option_displayed(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')
        self.prepare_savior_option_displayed(browser)
        try:
            implement_download_file(browser, get_current_download_folder, file_type='slow')
        finally:
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)


class TestMotPhim:

    def test_check_default_state_download_button(self, browser):
        pass


class TestTvZing:

    @pytestrail.case('C96763')
    def test_check_default_state_download_button(self, browser):
        pause_any_video_site(browser, OtherSiteUrls.TV_ZING_VIDEO_URL)
        savior_page_object.assert_value_preferred_quality(browser, 'High')
