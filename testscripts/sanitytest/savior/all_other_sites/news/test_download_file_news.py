from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import delete_all_mp4_file_download, \
    download_file_via_main_download_button, assert_file_download_value, clear_data_download
from utils_automation.const import OtherSiteUrls
from utils_automation.setup import WaitAfterEach

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()


class Test24H:

    @staticmethod
    def mouse_over_video_element_24h(browser):
        browser.get(OtherSiteUrls.TWENTY_FOUR_H_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_24h(browser)
        any_site_page_object.mouse_over_video_element_24h(browser)

    def prepare_check_download(self, browser, download_folder):
        self.mouse_over_video_element_24h(browser)
        # download_folder_path = self.setting_page_obeject.get_download_folder(browser)
        delete_all_mp4_file_download(download_folder, '.mp4')
        WaitAfterEach.sleep_timer_after_each_step()

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.mouse_over_video_element_24h(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_check_click_download_button_default_quality(self, browser, get_current_download_folder):
        self.prepare_check_download(browser, get_current_download_folder)
        try:
            download_file_via_main_download_button(browser)
            self.mouse_over_video_element_24h(browser)
            savior_page_object.choose_preferred_option(browser)
            height_frame = savior_page_object.verify_correct_video_options_chosen_high_quality_option(browser)
            # File mp4 file and assert
            assert_file_download_value(get_current_download_folder, height_frame)
        finally:
            clear_data_download(browser)


