import pytest
from pytest_testrail.plugin import pytestrail

from models.pagelocators.top_savior_sites.top_savior_sites_video_length import TopSaviorSitesVideoLengthLocators, \
    OnlineMusicVideoLengthLocators
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from models.pageobject.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthActions
from testscripts.common_setup import pause_any_video_site
from testscripts.savior_top_100_sites.common import download_and_verify_video
from utils_automation.const import OtherSiteUrls, VideoUrls

top_site_titles_action = TopSitesSaviorTitleAction()


class TestOnlineMusic:
    top_savior_sites_video_length_action = TopSitesSaviorVideoLengthActions()

    @pytestrail.case('C98782')
    @pytest.mark.one_hundred_popular_sites
    def test_download_nhac_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.NHAC_VN_VIDEO_URL)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, OnlineMusicVideoLengthLocators.NHAC_VN_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)



    @pytestrail.case('C96756')
    @pytest.mark.one_hundred_popular_sites
    def test_download_zing_mp3_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        pause_any_video_site(browser_top_sites, VideoUrls.ZING_MP3_VN_VIDEO_URL)
        self.any_site_page_object.click_zingmp3_chon_giao_dien_btn(browser_top_sites)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)