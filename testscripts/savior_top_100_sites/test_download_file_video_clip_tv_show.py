import logging

import pytest

from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail

from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from testscripts.common_setup import download_file_via_main_download_button, assert_file_download_value, \
    get_resolution_info
from testscripts.savior_top_100_sites.common import download_and_verify_video
from utils_automation.const import OtherSiteUrls

savior_page_object = SaviorPageObject()
any_site_page_object = AnySitePageObject()
top_site_titles_action = TopSitesSaviorTitleAction()

LOGGER = logging.getLogger(__name__)


class TestDailyMotion:
    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.DAILY_MOTION_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.DAILY_MOTION_VIDEO_URL)
        video_title_root = top_site_titles_action.get_website_title_by_javascript(browser)
        video_title_temp = top_site_titles_action.replace_special_characters_by_dash_in_string(video_title_root)
        video_title = top_site_titles_action.get_first_part_of_video_title(video_title_temp)
        any_site_page_object.mouse_over_video_item_daily_motion(browser)
        return video_title

    @pytestrail.case('C98793')
    @pytest.mark.one_hundred_popular_sites
    def test_download_file_daily_motion(self, browser_top_sites, get_current_download_folder_top_sites):
                                        # enable_fair_adblocker):
        video_title = self.prepare_savior_option_appear(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  video_title, mouse_over_first_video=False)



class TestVliveTV:

    @staticmethod
    def mouse_over_video_for_displaying_savior(browser):
        browser.get(OtherSiteUrls.VLIVE_TV_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_vlive_tv(browser)

    @pytestrail.case('C98809')
    def test_download_file_vlive_tv(self, browser_top_sites, get_current_download_folder_top_sites):
        self.mouse_over_video_for_displaying_savior(browser_top_sites)
        media_info = download_file_via_main_download_button(browser_top_sites)
        resolution_info = get_resolution_info(media_info)
        assert_file_download_value(get_current_download_folder, resolution_info)
