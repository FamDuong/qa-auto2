from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import delete_all_mp4_file_download, \
    clear_data_download, implement_download_file, \
    clear_data_download_in_browser_and_download_folder, verify_download_quality_high_frame
from utils_automation.const import OtherSiteUrls
from utils_automation.setup import WaitAfterEach

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()


class Test24H:

    @staticmethod
    def mouse_over_video_element_24h(browser):
        browser.get(OtherSiteUrls.TWENTY_FOUR_H_VIDEO_URL)
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
            verify_download_quality_high_frame(browser, get_current_download_folder,
                                               self.mouse_over_video_element_24h)
        finally:
            clear_data_download(browser)


class TestKienThucDotNet:

    @staticmethod
    def prepare_appear_savior_option(browser):
        browser.get(OtherSiteUrls.KIENTHUC_VIDEO_URL)
        WaitAfterEach.sleep_timer_after_each_step()
        # coords = pyautogui.locateOnScreen('video_item.PNG')
        # pyautogui.click(coords)
        any_site_page_object.click_video_item_kienthuc(browser)
        any_site_page_object.mouse_over_video_item_kienthuc(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.prepare_appear_savior_option(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_check_click_download_button_default_quality(self, browser, get_current_download_folder):
        self.prepare_appear_savior_option(browser)
        try:
            implement_download_file(browser, get_current_download_folder)
        finally:
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)


class TestVietnamNet:

    @staticmethod
    def prepare_savior_option_displayed(browser):
        browser.get(OtherSiteUrls.VIETNAMNET_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_vietnamnet(browser)

    @pytestrail.case('C54151')
    def test_check_default_state(self, browser):
        self.prepare_savior_option_displayed(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_check_click_download_button_default_quality(self, browser, get_current_download_folder):
        self.prepare_savior_option_displayed(browser)
        try:
            verify_download_quality_high_frame(browser, get_current_download_folder,
                                               self.prepare_savior_option_displayed)
        finally:
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)


class TestEvaVn:

    @staticmethod
    def prepare_savior_displayed(browser):
        browser.get(OtherSiteUrls.EVA_VN_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_eva_vn(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.prepare_savior_displayed(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_check_click_download_button_default_quality(self, browser, get_current_download_folder):
        self.prepare_savior_displayed(browser)
        try:
            verify_download_quality_high_frame(browser, get_current_download_folder,
                                               self.prepare_savior_displayed)
        finally:
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)


class TestSoha:

    @staticmethod
    def prepare_savior_displayed(browser):
        browser.get(OtherSiteUrls.SOHA_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_soha(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.prepare_savior_displayed(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_check_click_download_button_default_quality(self, browser, get_current_download_folder):
        self.prepare_savior_displayed(browser)
        try:
            verify_download_quality_high_frame(browser, get_current_download_folder,
                                               self.prepare_savior_displayed)
        finally:
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)


class Test2SaoVn:

    @staticmethod
    def prepare_savior_displayed(browser):
        browser.get(OtherSiteUrls.SAO_2_VN_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_sao_2_vn(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.prepare_savior_displayed(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_check_click_download_button_default_quality(self, browser, get_current_download_folder):
        self.prepare_savior_displayed(browser)
        try:
            verify_download_quality_high_frame(browser, get_current_download_folder,
                                               self.prepare_savior_displayed)
        finally:
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)


class TestPhuNuVaGiaDinh:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.PHUNU_GIADINH_VIDEO_URL)
        any_site_page_object.click_video_item_phunu_giadinh(browser)
        any_site_page_object.mouse_over_video_item_phunu_giadinh(browser)

    @pytestrail.case('C54151')
    def test_check_default_state_download_button(self, browser):
        self.prepare_savior_option_appear(browser)
        savior_page_object.assert_value_preferred_quality(browser, 'High')

    @pytestrail.case('C54152')
    def test_check_click_download_button_default_quality(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        try:
            implement_download_file(browser, get_current_download_folder)
        finally:
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)
