import logging
import pytest

from models.pagelocators.top_savior_sites.top_savior_sites_video_length import TopSaviorSitesVideoLengthLocators
from models.pagelocators.top_savior_sites.top_savior_sites_video_length import VideoClipTVShowVideoLengthLocators
# from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from models.pageobject.top_savior_sites.top_savior_sites_video_clip_tv_show import TopSaviorSitesVideoClipTvShowActions
from models.pageobject.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthActions
# from testscripts.common_setup import download_file_via_main_download_button, assert_file_download_value, \
#     get_resolution_info
from testscripts.savior_top_100_sites.common import download_and_verify_video
from utils_automation.const import OtherSiteUrls, VideoUrls

# savior_page_object = SaviorPageObject()

LOGGER = logging.getLogger(__name__)


class TestVideoClipTVShow:
    any_site_page_object = AnySitePageObject()
    top_savior_sites_video_length_action = TopSitesSaviorVideoLengthActions()
    top_savior_sites_video_clip_tv_show_action = TopSaviorSitesVideoClipTvShowActions()
    top_sites_savior_title_action = TopSitesSaviorTitleAction()

    @pytestrail.case('C96719')
    @pytest.mark.top_sites
    def test_download_youtube(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(VideoUrls.YOUTUBE_VIDEO_URL)
        LOGGER.info("Check download video on " + VideoUrls.YOUTUBE_VIDEO_URL)
        video_title = self.top_sites_savior_title_action.get_youtube_video_title(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesVideoLengthLocators.YOUTUBE_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

    # @pytestrail.case('C96763')
    # @pytest.mark.ten_popular_sites
    # def test_download_file_tv_zing(self, browser_top_sites, get_current_download_folder_top_sites):
    #     self.top_savior_sites_video_clip_tv_show_action.login_tv_zing(browser_top_sites)
    #     browser_top_sites.get(OtherSiteUrls.TV_ZING_VIDEO_URL)
    #     video_title = top_sites_savior_title_action.get_tv_zing_video_title(browser_top_sites)
    #     expect_length = top_savior_sites_video_length_action.get_video_length(browser_top_sites,
    #                                                                           TopSaviorSitesVideoLengthLocators.TV_ZING_VIDEO_LENGTH_CSS)
    #     download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

    @pytestrail.case('C98793')
    @pytest.mark.top_sites
    def test_download_file_daily_motion(self, browser_top_sites, get_current_download_folder_top_sites):
                                        # enable_fair_adblocker):
        browser_top_sites.get(OtherSiteUrls.DAILY_MOTION_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.DAILY_MOTION_VIDEO_URL)
        video_title_root = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        video_title_temp = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(video_title_root)
        video_title = self.top_sites_savior_title_action.get_first_part_of_video_title(video_title_temp)
        self.any_site_page_object.mouse_over_video_item_daily_motion(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
                                            get_video_length(browser_top_sites, VideoClipTVShowVideoLengthLocators.DAILY_MOTION_VIDEO_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length,
                                  start_with=video_title, mouse_over_first_video=False)
#
#
#
# class TestVliveTV:
#
#     @staticmethod
#     def mouse_over_video_for_displaying_savior(browser):
#         browser.get(OtherSiteUrls.VLIVE_TV_VIDEO_URL)
#         any_site_page_object.mouse_over_video_element_vlive_tv(browser)
#
#     @pytestrail.case('C98809')
#     def test_download_file_vlive_tv(self, browser_top_sites, get_current_download_folder_top_sites):
#         self.mouse_over_video_for_displaying_savior(browser_top_sites)
#         media_info = download_file_via_main_download_button(browser_top_sites)
#         resolution_info = get_resolution_info(media_info)
#         assert_file_download_value(get_current_download_folder, resolution_info)
