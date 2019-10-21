import pytest
from pytest_testrail.plugin import pytestrail

from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from testscripts.sanitytest.savior.common_setup import verify_video_step_then_clear_data, implement_download_file, \
    clear_data_download_in_browser_and_download_folder
from utils_automation.const import OtherSiteUrls
from utils_automation.setup import WaitAfterEach

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()


class TestXVideos:

    @pytestrail.case('C96723')
    @pytest.mark.ten_popular_sites
    def test_download_file_x_videos(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.XVIDEOS_DOT_COM_VIDEO_URL)
        any_site_page_object.mouse_over_video_x_videos(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='very slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestXNXX:

    @pytestrail.case('C96754')
    @pytest.mark.ten_popular_sites
    def test_download_file_x_videos(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.XNXX_VIDEO_URL)
        any_site_page_object.mouse_over_video_xnxx(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='very slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestPornHub:

    @pytestrail.case('C98771')
    @pytest.mark.ten_popular_sites
    def test_download_file_x_videos(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.FR_PORN_HUB_VIDEO_URL)
        any_site_page_object.mouse_over_video_fr_porn_hub(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestVLXX:

    @pytestrail.case('C96762')
    def test_download_file_vlxx_videos(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.VLXX_VIDEO_URL)
        any_site_page_object.click_video_vlxx(browser)
        any_site_page_object.mouse_over_video_vlxx(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestSexTop1:

    @pytestrail.case('C98726')
    def test_download_file_sex_top1_video(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.SEX_TOP1_VIDEO_URL)
        any_site_page_object.click_video_sex_top1(browser)
        any_site_page_object.mouse_over_video_sex_top1(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='very slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestSexHiHi:

    @pytestrail.case('C98731')
    def test_download_file_sex_hihi_video(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.SEX_HIHI_VIDEO_URL)
        WaitAfterEach.sleep_timer_after_each_step()
        any_site_page_object.click_video_sex_hihi(browser)
        any_site_page_object.mouse_over_video_sex_hihi(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='very slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestJavHdPro:

    @pytestrail.case('C98744')
    def test_download_file_jav_hd_pro(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.JAV_HD_PRO_VIDEO_URL)
        any_site_page_object.click_video_jav_hd_pro(browser)
        any_site_page_object.mouse_over_video_jav_hd_pro(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='very slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestPhimSexPorn:

    @pytestrail.case('C98774')
    def test_download_file_phim_sex_porn(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.PHIM_SEX_PORN_VIDEO_URL)
        any_site_page_object.click_video_phim_sex_porn(browser)
        any_site_page_object.mouse_over_video_phim_sex_porn(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestJavaPhim:

    @pytestrail.case('C98783')
    def test_download_file_java_phim(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.JAV_PHIM_VIDEO_URL)
        any_site_page_object.click_video_jav_phim(browser)
        any_site_page_object.mouse_over_video_jav_phim(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestSexNgon:

    @pytestrail.case('C98799')
    def test_download_file_sex_ngon(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.SEX_NGON_VIDEO_URL)
        any_site_page_object.click_video_element_sex_ngon(browser)
        any_site_page_object.mouse_over_video_element_sex_ngon(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))


class TestPhimSexSub:

    @pytestrail.case('C98806')
    def test_download_file_phim_sex_sub(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.PHIM_SEX_SUB_VIDEO_URL)
        any_site_page_object.click_video_phim_sex_sub_video_element(browser)
        any_site_page_object.mouse_over_video_element_phim_sex_sub(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='slow'),
            clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder))















