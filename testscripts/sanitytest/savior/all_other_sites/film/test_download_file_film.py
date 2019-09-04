import pytest
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import download_file_via_main_download_button, clear_data_download, \
    assert_file_download_value, implement_download_file, clear_data_download_in_browser_and_download_folder
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
        self.pause_video_element_phimmoi(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.prepare_displayed_savior_popup(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    @pytest.mark.skip(reason='Unstable for downloading file')
    def test_check_click_download_button_default_quality(self, browser, get_current_download_folder):
        self.prepare_displayed_savior_popup(browser)
        try:
            download_file_via_main_download_button(browser, file_type='movie')
            self.prepare_displayed_savior_popup(browser)
            savior_page_object.choose_preferred_option(browser)
            height_frame = savior_page_object.verify_correct_video_options_chosen_high_quality_option(browser)
        # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)

        finally:
            clear_data_download(browser)


class TestVuViPhim:

    @staticmethod
    def prepare_savior_option_displayed(browser):
        browser.get(OtherSiteUrls.VU_VI_PHIM_VIDEO_URL)
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        any_site_page_object.click_video_item_vu_vi_phim(browser)
        any_site_page_object.mouse_over_video_item_vu_vi_phim(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.prepare_savior_option_displayed(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_check_click_download_button_default_quality(self, browser, get_current_download_folder):
        self.prepare_savior_option_displayed(browser)
        try:
            implement_download_file(browser, get_current_download_folder, file_type='slow')
        finally:
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)


class TestMotPhim:

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        pass




