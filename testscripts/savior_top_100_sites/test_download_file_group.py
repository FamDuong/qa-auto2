import logging

import pytest
from models.pageobject.savior import SaviorPageObject
from pytest_testrail.plugin import pytestrail
from models.pageobject.sites import AnySitePageObject, YoutubePageObject
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from testscripts.common_setup import pause_any_video_site, download_file_via_main_download_button, \
    assert_file_download_value, delete_all_mp4_file_download, \
    implement_download_file, get_resolution_info, pause_or_play_video_by_javascript
from utils_automation.const import VideoUrls
from utils_automation.setup import WaitAfterEach
from testscripts.savior_top_100_sites.common import download_and_verify_video


LOGGER = logging.getLogger(__name__)


class TestDownloadGroup:
    savior_page_object = SaviorPageObject()
    any_site_page_object = AnySitePageObject()
    top_site_titles_action = TopSitesSaviorTitleAction()

    # @staticmethod
    # def prepare_check_download(download_folder):
    #     delete_all_mp4_file_download(download_folder, '.mp4')
    #     WaitAfterEach.sleep_timer_after_each_step()
    #
    # def implement_test_site(self, browser, url_site, get_current_download_folder):
    #     try:
    #         pause_any_video_site(browser, url_site)
    #         video_title = top_site_titles_action.get_website_title_by_javascript(browser)
    #         media_info = download_file_via_main_download_button(browser, time_sleep=10)
    #         resolution_info = get_resolution_info(media_info)
    #         assert_file_download_value(get_current_download_folder, resolution_info, video_title)
    #     finally:
    #         delete_all_mp4_file_download(get_current_download_folder, '.mp4', startwith=video_title)

    @pytestrail.case('C96719')
    @pytest.mark.ten_popular_sites
    def test_download_youtube(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(VideoUrls.YOUTUBE_VIDEO_URL)
        video_title = self.top_site_titles_action.get_youtube_video_title(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

    @pytestrail.case('C96752')
    def test_download_news_zing(self, browser_top_sites, get_current_download_folder_top_sites):
        pause_any_video_site(browser_top_sites, VideoUrls.NEWS_ZING_VIDEO_URL)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

    @pytestrail.case('C96756')
    def test_download_zing_mp3_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        pause_any_video_site(browser_top_sites, VideoUrls.ZING_MP3_VN_VIDEO_URL)
        self.any_site_page_object.click_zingmp3_chon_giao_dien_btn(browser_top_sites)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)
        #
        # self.implement_test_site(browser_top_sites, VideoUrls.ZING_MP3_VN_VIDEO_URL,
        #                          get_current_download_folder_top_sites)

    @pytestrail.case('C96758')
    @pytest.mark.ten_popular_sites
    def test_download_nhaccuatui(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(VideoUrls.NHAC_CUA_TUI_VIDEO_ITEM)
        video_title = self.top_site_titles_action.get_nhaccuatui_video_title(browser_top_sites)
        self.any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        media_info = download_file_via_main_download_button(browser_top_sites, time_sleep=15)
        resolution_info = get_resolution_info(media_info)
        try:
            assert_file_download_value(get_current_download_folder_top_sites, resolution_info,
                                       start_with=video_title)
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title)

    # @pytestrail.case('C98735')
    # @pytest.mark.ten_popular_sites
    # @pytestrail.defect('PF-517')
    # def test_download_dongphim(self, browser_top_sites, get_current_download_folder_top_sites):
    #     try:
    #         browser_top_sites.get(VideoUrls.DONG_PHIM_VIDEO_URL)
    #         pause_or_play_video_by_javascript(browser_top_sites, action='play')
    #         any_site_page_object.click_first_video_element(browser_top_sites)
    #         any_site_page_object.mouse_over_first_video_element(browser_top_sites)
    #         video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
    #         implement_download_file(browser_top_sites, get_current_download_folder_top_sites, time_sleep=10)
    #     finally:
    #         delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title)
    # browser_top_sites.get(VideoUrls.DONG_PHIM_VIDEO_URL)
    # elements = any_site_page_object.choose_watch_option_if_any(browser_top_sites)
    # video_title_start_with = 'Thi'
    # if len(elements) == 0:
    #     any_site_page_object.click_video_item_dong_phim(browser_top_sites)
    # any_site_page_object.mouse_over_video_item_dong_phim(browser_top_sites)
    # try:
    #     implement_download_file(browser_top_sites, get_current_download_folder_top_sites, file_size=50.00,
    #                             startwith=video_title_start_with)
    # finally:
    #     delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title_start_with)
