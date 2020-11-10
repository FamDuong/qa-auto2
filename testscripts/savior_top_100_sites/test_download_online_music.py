import logging

import pytest
from pytest_testrail.plugin import pytestrail
from models.pagelocators.top_savior_sites.top_savior_sites_video_length import TopSaviorSitesVideoLengthLocators, \
    OnlineMusicVideoLengthLocators
from models.pageobject.sites import AnySitePageObject
from models.pageobject.top_savior_sites.top_savior_sites_online_music import TopSaviorSitesOnlineMusicActions
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from models.pageobject.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthActions
from testscripts.common_setup import pause_any_video_site
from testscripts.savior_top_100_sites.common import download_and_verify_video
from utils_automation.const import OnlineMusicUrls

LOGGER = logging.getLogger(__name__)


class TestOnlineMusic:
    any_site_page_object = AnySitePageObject()
    top_sites_savior_title_action = TopSitesSaviorTitleAction()
    top_savior_sites_video_length_action = TopSitesSaviorVideoLengthActions()
    top_savior_sites_online_music_action = TopSaviorSitesOnlineMusicActions()

    @pytestrail.case('C96758')
    @pytest.mark.top_sites
    def test_download_nhaccuatui(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OnlineMusicUrls.NHAC_CUA_TUI_VIDEO_ITEM)
        LOGGER.info("Check download video on " + OnlineMusicUrls.NHAC_CUA_TUI_VIDEO_ITEM)
        self.top_savior_sites_online_music_action.click_on_nhac_cua_tui_marketing_popup(browser_top_sites)

        video_title = self.top_sites_savior_title_action.get_nhaccuatui_video_title(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites,
                             TopSaviorSitesVideoLengthLocators.NHACCUATUI_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

        browser_top_sites.get(OnlineMusicUrls.NHAC_CUA_TUI_MUSIC_ITEM)
        LOGGER.info("Check download music on " + OnlineMusicUrls.NHAC_CUA_TUI_MUSIC_ITEM)
        video_title = self.top_sites_savior_title_action.get_nhaccuatui_video_title(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites,
                             TopSaviorSitesVideoLengthLocators.NHACCUATUI_MP3_LENGTH_CSS)
        self.any_site_page_object.mouse_over_nhaccuatui_music_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length,
                                  video_title, end_with='.mp3', mouse_over_first_video=False)

    @pytestrail.case('C98760')
    @pytest.mark.top_sites
    def test_download_soundcloud(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OnlineMusicUrls.SOUNDCLOUD_URL)
        LOGGER.info("Check download music on " + OnlineMusicUrls.SOUNDCLOUD_URL)

        video_title = self.top_sites_savior_title_action.get_soundcloud_music_title(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, OnlineMusicVideoLengthLocators.SOUNDCLOUD_MP3_LENGTH_CSS)
        self.any_site_page_object.mouse_over_soundcloud_music_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length,
                                  video_title, end_with='.mp3', mouse_over_first_video=False)

    @pytestrail.case('C98782')
    @pytest.mark.others
    def test_download_nhac_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OnlineMusicUrls.NHAC_VN_VIDEO_URL)
        LOGGER.info("Check download music on " + OnlineMusicUrls.NHAC_VN_VIDEO_URL)
        video_title = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, OnlineMusicVideoLengthLocators.NHAC_VN_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

    @pytestrail.case('C96756')
    @pytest.mark.others
    def test_download_zing_mp3_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        from unidecode import unidecode
        browser_top_sites.get(OnlineMusicUrls.ZING_MP3_VN_VIDEO_URL)
        LOGGER.info("Check download music on " + OnlineMusicUrls.ZING_MP3_VN_VIDEO_URL)
        self.any_site_page_object.click_zingmp3_chon_giao_dien_btn(browser_top_sites)
        video_title_root = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        video_title = unidecode(self.top_sites_savior_title_action.get_first_part_of_video_title(video_title_root)).strip()
        LOGGER.info("Video title: "+video_title)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, OnlineMusicVideoLengthLocators.ZING_MP3_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)
