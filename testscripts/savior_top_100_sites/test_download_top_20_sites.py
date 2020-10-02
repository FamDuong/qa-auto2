import logging
import time

import pytest

from pytest_testrail.plugin import pytestrail
from models.pageobject.sites import AnySitePageObject
from models.pageobject.top_savior_sites.top_savior_sites_film import TopSaviorSitesFilmActions
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from testscripts.savior_top_100_sites.test_download_file_social_network import top_sites_savior_title_actions
from utils_automation.const import VideoUrls, OtherSiteUrls
from testscripts.savior_top_100_sites.common import download_and_verify_video, choose_highest_resolution_of_video, \
    login_facebook
from testscripts.common_setup import assert_file_download_value, delete_all_mp4_file_download, \
    download_file_via_main_download_button, get_resolution_info, implement_download_file

LOGGER = logging.getLogger(__name__)


class TestDownloadTop20Sites:
    any_site_page_object = AnySitePageObject()
    top_sites_savior_title_action = TopSitesSaviorTitleAction()
    top_savior_sites_film_action = TopSaviorSitesFilmActions()

    @pytestrail.case('C96719')
    @pytest.mark.twenty_popular_sites
    def test_download_youtube(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(VideoUrls.YOUTUBE_VIDEO_URL)
        LOGGER.info("Check download video on "+VideoUrls.YOUTUBE_VIDEO_URL)
        video_title = self.top_sites_savior_title_action.get_youtube_video_title(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

    @pytestrail.case('C96758')
    @pytest.mark.twenty_popular_sites
    def test_download_nhaccuatui(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(VideoUrls.NHAC_CUA_TUI_VIDEO_ITEM)
        LOGGER.info("Check download video on " + VideoUrls.NHAC_CUA_TUI_VIDEO_ITEM)
        video_title = self.top_sites_savior_title_action.get_nhaccuatui_video_title(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

        browser_top_sites.get(VideoUrls.NHAC_CUA_TUI_MUSIC_ITEM)
        LOGGER.info("Check download video on " + VideoUrls.NHAC_CUA_TUI_MUSIC_ITEM)
        video_title = self.top_sites_savior_title_action.get_nhaccuatui_video_title(browser_top_sites)
        self.any_site_page_object.mouse_over_nhaccuatui_music_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  video_title,  end_with='.mp3', mouse_over_first_video=False)

    def verify_download_file_facebook_by_url(self, driver, download_folder, url):
        driver.get(url)
        LOGGER.info("Check download video on " + url)
        self.any_site_page_object.mouse_over_first_video_element(driver)
        choose_highest_resolution_of_video(driver)
        video_title_temp = self.top_sites_savior_title_action.get_video_title_from_filename_span_tag(driver)
        video_title = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(video_title_temp)
        media_info = download_file_via_main_download_button(driver, video_title)
        resolution_info = get_resolution_info(media_info)
        try:
            assert_file_download_value(download_folder, resolution_info, start_with=video_title,
                                       end_with=".mp4")
        finally:
            pass
            # delete_all_mp4_file_download(download_folder, end_with=".mp4", start_with=video_title)

    @pytestrail.case('C96691')
    @pytest.mark.twenty_popular_sitesmotphim
    def test_download_file_facebook(self, browser_top_sites, get_current_download_folder_top_sites):
        self.verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
                                                  OtherSiteUrls.FACEBOOK_VIDEO_URL)
        # login_facebook(browser_top_sites)
        # browser_top_sites.get(OtherSiteUrls.FACEBOOK_VIDEO_URL)
        # LOGGER.info("Check download video on " + OtherSiteUrls.FACEBOOK_VIDEO_URL)
        # # time.sleep(3)
        # self.any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        # choose_highest_resolution_of_video(browser_top_sites)
        # # time.sleep(3)
        # video_title_temp = self.top_site_savior_title_action.get_facebook_video_title(browser_top_sites)
        # video_title = self.top_site_savior_title_action.replace_special_characters_by_dash_in_string(video_title_temp)
        # media_info = download_file_via_main_download_button(browser_top_sites, video_title)
        # resolution_info = get_resolution_info(media_info)
        # try:
        #     assert_file_download_value(get_current_download_folder_top_sites, resolution_info, start_with=video_title, end_with=".mp4")
        # finally:
        #     delete_all_mp4_file_download(get_current_download_folder_top_sites, end_with=".mp4", start_with=video_title)


        # download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

    @pytestrail.case('C204280')
    @pytest.mark.twenty_popular_sites
    def test_download_ok_ru(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.OK_RU)
        LOGGER.info("Check download video on " + OtherSiteUrls.OK_RU)
        video_title = top_sites_savior_title_actions.get_ok_ru_video_title(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

    @pytestrail.case('C98735')
    @pytest.mark.ten_popular_sites
    @pytestrail.defect('PF-517')
    def test_download_dongphim(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(VideoUrls.DONG_PHIM_VIDEO_URL)
        LOGGER.info("Check download video on " + VideoUrls.DONG_PHIM_VIDEO_URL)
        elements = self.any_site_page_object.choose_watch_option_if_any(browser_top_sites)
        if len(elements) == 0:
            self.any_site_page_object.click_video_item_dong_phim(browser_top_sites)
        video_title = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

    def verify_download_file_title_get_after_download(self, driver, download_folder, url):
        driver.get(url)
        LOGGER.info("Check download video on " + url)
        self.any_site_page_object.mouse_over_first_video_element(driver)
        choose_highest_resolution_of_video(driver)
        video_title_temp = self.top_sites_savior_title_action.get_video_title_from_filename_span_tag(driver)
        video_title = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(video_title_temp)
        media_info = download_file_via_main_download_button(driver, video_title)
        resolution_info = get_resolution_info(media_info)
        try:
            assert_file_download_value(download_folder, resolution_info, start_with=video_title,
                                       end_with=".mp4")
        finally:
            pass

    @pytestrail.case('C98756')
    @pytestrail.defect('PF-541')
    def test_download_file_film_mot_phim_net(self, browser_top_sites, get_current_download_folder_top_sites):
        LOGGER.info("Check download video on " + OtherSiteUrls.MOT_PHIM_VIDEO_URL)
        time.sleep(2)
        browser_top_sites.refresh()
        self.any_site_page_object.mouse_over_video_item_mot_phim(browser_top_sites)
        choose_highest_resolution_of_video(browser_top_sites)
        video_title_temp = self.top_sites_savior_title_action.get_video_title_from_filename_span_tag(browser_top_sites)
        video_title = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(video_title_temp)
        media_info = download_file_via_main_download_button(browser_top_sites, video_title)
        resolution_info = get_resolution_info(media_info)
        try:
            assert_file_download_value(get_current_download_folder_top_sites, resolution_info, start_with=video_title,
                                       end_with=".mp4")
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, end_with=".mp4", start_with=video_title)

        # browser.get(OtherSiteUrls.MOT_PHIM_VIDEO_URL)
        # time.sleep(2)
        # self.any_site_page_object.click_video_item_mot_phim(browser)
        # time.sleep(5)
        # self.any_site_page_object.mouse_over_video_item_mot_phim(browser, url=OtherSiteUrls.MOT_PHIM_VIDEO_URL)
        # implement_download_file(browser, get_current_download_folder, )

    @pytestrail.case('C96763')
    @pytest.mark.ten_popular_sites
    def test_download_file_tv_zing(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.TV_ZING_VIDEO_URL)
        self.top_savior_sites_film_action.close_login_popup_tv_zing(browser_top_sites)
        video_title = self.top_sites_savior_title_action.get_tv_zing_video_title(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)



    def prepare_appear_savior_option(self, browser):
        browser.get(OtherSiteUrls.INSTAGRAM_VIDEO_URL)
        self.any_site_page_object.mouse_over_video_element_instagram(browser)

    @pytestrail.case('C96751')
    @pytest.mark.ten_popular_sites
    def test_download_file_instagram(self, browser_top_sites, get_current_download_folder_top_sites):
        self.prepare_appear_savior_option(browser_top_sites)
        from textwrap import wrap
        video_title_start_with = wrap(top_sites_savior_title_actions.get_instagram_video_title(browser_top_sites), 6)[0]
        try:
            implement_download_file(browser_top_sites, get_current_download_folder_top_sites, startwith=video_title_start_with),
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title_start_with)
