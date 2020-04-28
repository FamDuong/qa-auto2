import time

import pytest
from models.pageobject.savior import SaviorPageObject
from pytest_testrail.plugin import pytestrail
from models.pageobject.sites import AnySitePageObject, YoutubePageObject
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from testscripts.common_setup import pause_any_video_site, download_file_via_main_download_button, \
    assert_file_download_value, delete_all_mp4_file_download, \
    implement_download_file, get_resolution_info
from utils_automation.const import VideoUrls
from utils_automation.setup import WaitAfterEach

any_site_page_object = AnySitePageObject()
top_site_titles_action = TopSitesSaviorTitleAction()


class TestDownloadGroup:
    savior_page_object = SaviorPageObject()

    @staticmethod
    def prepare_check_download(download_folder):
        delete_all_mp4_file_download(download_folder, '.mp4')
        WaitAfterEach.sleep_timer_after_each_step()

    def implement_test_site(self, browser, url_site, get_current_download_folder, **kwargs):
        pause_any_video_site(browser, url_site)
        self.prepare_check_download(get_current_download_folder)
        media_info = download_file_via_main_download_button(browser, )
        resolution_info = get_resolution_info(media_info)
        assert_file_download_value(get_current_download_folder, resolution_info, **kwargs)

    @pytestrail.case('C96719')
    @pytestrail.defect('PF-776', 'PF-1095')
    @pytest.mark.ten_popular_sites
    def test_download_youtube(self, browser_top_sites, get_current_download_folder_top_sites, clear_download_page):
        youtube_page_object = YoutubePageObject()
        browser_top_sites.get(VideoUrls.YOUTUBE_VIDEO_URL)
        video_title = top_site_titles_action.get_youtube_video_title(browser_top_sites)
        youtube_page_object.mouse_over_video_item(browser_top_sites)
        media_info = download_file_via_main_download_button(browser_top_sites, )
        resolution_info = get_resolution_info(media_info)
        try:
            assert_file_download_value(get_current_download_folder_top_sites, resolution_info, startwith=video_title)
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title)

    @pytestrail.case('C96752')
    def test_download_news_zing(self, browser_top_sites, get_current_download_folder_top_sites, clear_download_page):
        self.implement_test_site(browser_top_sites, VideoUrls.NEWS_ZING_VIDEO_URL, get_current_download_folder_top_sites)

    @pytestrail.case('C96756')
    def test_download_zing_mp3_vn(self, browser_top_sites, get_current_download_folder_top_sites, clear_download_page):
        self.implement_test_site(browser_top_sites, VideoUrls.ZING_MP3_VN_VIDEO_URL, get_current_download_folder_top_sites)

    @pytestrail.case('C96758')
    @pytest.mark.ten_popular_sites
    def test_download_nhaccuatui(self, browser_top_sites, get_current_download_folder_top_sites, clear_download_page):
        video_title_start_with = "NIOEH,"
        browser_top_sites.get(VideoUrls.NHAC_CUA_TUI_VIDEO_ITEM)
        time.sleep(3)
        try:
            browser_top_sites.execute_script('document.querySelector("div.vjs-control-bar > button.vjs-play-control.vjs-control.vjs-button").click();')
        except Exception as e:
            print(e)
        if any_site_page_object.check_if_nhac_cua_tui_ads_appeared(driver=browser_top_sites) > 0:
            time.sleep(2)
            try:
                browser_top_sites.execute_script('document.querySelector("div.vjs-control-bar > button.vjs-play-control.vjs-control.vjs-button.vjs-paused").click();')
            except Exception as e:
                print(e)
            try:
                browser_top_sites.execute_script('document.querySelector("#video_vpaid1587957395244 > div.vjs-control-bar > button.vjs-play-control.vjs-control.vjs-button").click();')
            except Exception as e:
                print(e)
            any_site_page_object.close_nhac_cua_tui_ad_item(driver=browser_top_sites)
            browser_top_sites.execute_script('document.querySelector("div.vast-skip-button.enabled").click();')
            time.sleep(1)
        any_site_page_object.click_first_video_element(browser_top_sites)
        any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        try:
            implement_download_file(browser_top_sites, get_current_download_folder_top_sites, time_sleep=10)
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title_start_with)

    @pytestrail.case('C98735')
    @pytest.mark.ten_popular_sites
    @pytestrail.defect('PF-517')
    def test_download_dongphim(self, browser_top_sites, get_current_download_folder_top_sites, clear_download_page):
        browser_top_sites.get(VideoUrls.DONG_PHIM_VIDEO_URL)
        elements = any_site_page_object.choose_watch_option_if_any(browser_top_sites)
        video_title_start_with = 'Thi'
        if len(elements) == 0:
            any_site_page_object.click_video_item_dong_phim(browser_top_sites)
        any_site_page_object.mouse_over_video_item_dong_phim(browser_top_sites)
        try:
            implement_download_file(browser_top_sites, get_current_download_folder_top_sites, file_size=50.00,
                                    startwith=video_title_start_with)
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title_start_with)
