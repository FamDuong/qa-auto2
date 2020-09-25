import logging
import pytest

from pytest_testrail.plugin import pytestrail
from models.pageobject.sites import AnySitePageObject
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from testscripts.common_setup import pause_any_video_site
from utils_automation.const import VideoUrls
from testscripts.savior_top_100_sites.common import download_and_verify_video

LOGGER = logging.getLogger(__name__)


class TestDownloadGroup:
    any_site_page_object = AnySitePageObject()
    top_site_titles_action = TopSitesSaviorTitleAction()

    @pytestrail.case('C96719')
    # @pytest.mark.ten_popular_sites
    @pytest.mark.one_hundred_popular_sites
    def test_download_youtube(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(VideoUrls.YOUTUBE_VIDEO_URL)
        video_title = self.top_site_titles_action.get_youtube_video_title(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

    @pytestrail.case('C96752')
    @pytest.mark.one_hundred_popular_sites
    def test_download_news_zing(self, browser_top_sites, get_current_download_folder_top_sites):
        pause_any_video_site(browser_top_sites, VideoUrls.NEWS_ZING_VIDEO_URL)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

    @pytestrail.case('C96756')
    @pytest.mark.one_hundred_popular_sites
    def test_download_zing_mp3_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        pause_any_video_site(browser_top_sites, VideoUrls.ZING_MP3_VN_VIDEO_URL)
        self.any_site_page_object.click_zingmp3_chon_giao_dien_btn(browser_top_sites)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

    @pytestrail.case('C96758')
    # @pytest.mark.ten_popular_sites
    @pytest.mark.one_hundred_popular_sites
    def test_download_nhaccuatui(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(VideoUrls.NHAC_CUA_TUI_VIDEO_ITEM)
        video_title = self.top_site_titles_action.get_nhaccuatui_video_title(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)
