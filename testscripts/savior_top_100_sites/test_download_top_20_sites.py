import logging
import time

import pytest
from pytest_testrail.plugin import pytestrail

from models.pagelocators.top_savior_sites.top_savior_sites_social import FacebookLocators, InstagramLocators
from models.pagelocators.top_savior_sites.top_savior_sites_video_length import TopSaviorSitesVideoLengthLocators, \
    VideoClipTVShowVideoLengthLocators, OnlineMusicVideoLengthLocators, SocialNetworkVideoLengthLocators
from models.pageobject.sites import AnySitePageObject
from models.pageobject.top_savior_sites.top_savior_sites_film import TopSaviorSitesFilmActions
from models.pageobject.top_savior_sites.top_savior_sites_online_music import TopSaviorSitesOnlineMusicActions
from models.pageobject.top_savior_sites.top_savior_sites_social import FacebookActions, InstagramActions
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from models.pageobject.top_savior_sites.top_savior_sites_video_clip_tv_show import TopSaviorSitesVideoClipTvShowActions
from models.pageobject.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthActions
from testscripts.common_setup import download_file_via_main_download_button, get_resolution_info, \
    assert_file_download_value, delete_all_mp4_file_download, pause_or_play_video_by_javascript
from testscripts.savior_top_100_sites.common import download_and_verify_video, choose_highest_resolution_of_video, \
    verify_download_file_facebook_by_url, login_instagram
from utils_automation.const import TopSitesUrls, OtherSiteUrls

LOGGER = logging.getLogger(__name__)


class TestTop20Sites:
    top_savior_sites_video_length_action = TopSitesSaviorVideoLengthActions()
    top_sites_savior_title_action = TopSitesSaviorTitleAction()
    top_savior_sites_online_music_action = TopSaviorSitesOnlineMusicActions()
    top_sites_savior_title_action = TopSitesSaviorTitleAction()
    any_site_page_object = AnySitePageObject()
    top_savior_sites_video_clip_tv_show_action = TopSaviorSitesVideoClipTvShowActions()
    facebook_action = FacebookActions()
    instagram_action = InstagramActions()
    any_site_page_object = AnySitePageObject()
    top_sites_savior_title_action = TopSitesSaviorTitleAction()
    top_savior_sites_film_action = TopSaviorSitesFilmActions()
    top_savior_sites_video_length_action = TopSitesSaviorVideoLengthActions()

    @pytestrail.case('C96719')
    @pytest.mark.top_sites
    def test_download_youtube(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(TopSitesUrls.YOUTUBE_VIDEO_URL)
        LOGGER.info("Check download video on " + TopSitesUrls.YOUTUBE_VIDEO_URL)
        video_title = self.top_sites_savior_title_action.get_youtube_video_title(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesVideoLengthLocators.YOUTUBE_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

    @pytestrail.case('C96758')
    @pytest.mark.top_sites
    def test_download_nhaccuatui(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(TopSitesUrls.NHAC_CUA_TUI_VIDEO_ITEM)
        LOGGER.info("Check download video on " + TopSitesUrls.NHAC_CUA_TUI_VIDEO_ITEM)
        self.top_savior_sites_online_music_action.click_on_nhac_cua_tui_marketing_popup(browser_top_sites)

        video_title = self.top_sites_savior_title_action.get_nhaccuatui_video_title(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites,
                             TopSaviorSitesVideoLengthLocators.NHACCUATUI_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

        browser_top_sites.get(TopSitesUrls.NHAC_CUA_TUI_MUSIC_ITEM)
        LOGGER.info("Check download music on " + TopSitesUrls.NHAC_CUA_TUI_MUSIC_ITEM)
        video_title = self.top_sites_savior_title_action.get_nhaccuatui_video_title(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites,
                             TopSaviorSitesVideoLengthLocators.NHACCUATUI_MP3_LENGTH_CSS)
        self.any_site_page_object.mouse_over_nhaccuatui_music_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length,
                                  video_title, end_with='.mp3', mouse_over_first_video=False)

    @pytestrail.case('C96691')
    @pytestrail.defect('PF-530')
    @pytest.mark.top_sites
    def test_download_file_facebook(self, browser_top_sites, get_current_download_folder_top_sites):

        # verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
        #                                      TopSitesUrls.FACEBOOK_HOMEPAGE_URL)
        verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
                                             TopSitesUrls.FACEBOOK_PROFILE_ME_URL)
        # verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
        #                                           TopSitesUrls.FACEBOOK_VTVGIAITRI_PAGE_URL)
        #
        # verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
        #                                           TopSitesUrls.FACEBOOK_WATCH_URL, need_opened_video=True,
        #                                           need_mouse_over_video=True)
        #
        # verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
        #                                           TopSitesUrls.FACEBOOK_WATCH_URL)
        # verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
        #                                           TopSitesUrls.FACEBOOK_VIDEO_URL)

    def download_file_tiktok(self, driver, download_folder, menu, is_login=False):
        driver.get(TopSitesUrls.TIKTOK_FOR_YOU_URL)
        if is_login:
            self.top_savior_sites_video_clip_tv_show_action.login_tiktok(driver)
        self.top_savior_sites_video_clip_tv_show_action.click_tiktok_menu(driver, menu)
        self.top_savior_sites_video_clip_tv_show_action.click_tiktok_first_video(driver, menu)
        LOGGER.info("Check download video on " + str(driver.current_url))
        video_title_root = self.top_sites_savior_title_action.get_tiktok_video_title(driver, menu)
        video_title_temp = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(
            video_title_root)
        video_title = self.top_sites_savior_title_action.get_first_part_of_video_title(video_title_temp)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(driver, VideoClipTVShowVideoLengthLocators.TIKTOK_VIDEO_CSS,
                             element="", url=TopSitesUrls.TIKTOK_FOR_YOU_URL)
        download_and_verify_video(driver, download_folder, expect_length, video_title)
        if menu == 'Following':
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    @pytestrail.case('C410745')
    @pytest.mark.top_sites
    def test_download_file_tiktok(self, browser_top_sites, get_current_download_folder_top_sites):
        self.download_file_tiktok(browser_top_sites, get_current_download_folder_top_sites,
                                  menu='For You', is_login=False)
        self.download_file_tiktok(browser_top_sites, get_current_download_folder_top_sites,
                                  menu='Following', is_login=False)
        self.download_file_tiktok(browser_top_sites, get_current_download_folder_top_sites,
                                  menu='For You', is_login=True)
        self.download_file_tiktok(browser_top_sites, get_current_download_folder_top_sites,
                                  menu='Following', is_login=True)

    @pytestrail.case('C204280')
    @pytest.mark.top_sites
    def test_download_ok_ru(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(TopSitesUrls.OK_RU)
        LOGGER.info("Check download video on " + TopSitesUrls.OK_RU)
        video_title = self.top_sites_savior_title_action.get_ok_ru_video_title(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites,
                             TopSaviorSitesVideoLengthLocators.OK_RU_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

    @pytestrail.case('C98760')
    @pytest.mark.top_sites
    def test_download_soundcloud(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(TopSitesUrls.SOUNDCLOUD_URL)
        LOGGER.info("Check download music on " + TopSitesUrls.SOUNDCLOUD_URL)

        video_title = self.top_sites_savior_title_action.get_soundcloud_music_title(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, OnlineMusicVideoLengthLocators.SOUNDCLOUD_MP3_LENGTH_CSS)
        self.any_site_page_object.mouse_over_soundcloud_music_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length,
                                  video_title, end_with='.mp3', mouse_over_first_video=False)

    @pytestrail.case('C98735')
    @pytest.mark.top_sites
    def test_download_dongphim(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(TopSitesUrls.DONG_PHIM_VIDEO_URL)
        LOGGER.info("Check download video on " + TopSitesUrls.DONG_PHIM_VIDEO_URL)
        elements = self.any_site_page_object.choose_watch_option_if_any(browser_top_sites)
        if len(elements) == 0:
            self.any_site_page_object.click_video_item_dong_phim(browser_top_sites)
        video_title = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesVideoLengthLocators.DONG_PHYM_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

    # def prepare_appear_savior_option(self, browser):
    #     browser.get(TopSitesUrls.INSTAGRAM_VIDEO_URL)
    #     self.any_site_page_object.mouse_over_video_element_instagram(browser)

    @pytestrail.case('C96751')
    @pytestrail.defect('PF-2074')
    @pytest.mark.top_sites
    def test_download_file_instagram(self, browser_top_sites, get_current_download_folder_top_sites):
        login_instagram(browser_top_sites)
        browser_top_sites.get(TopSitesUrls.INSTAGRAM_URL)
        LOGGER.info("Check download video on " + TopSitesUrls.INSTAGRAM_URL)
        self.instagram_action.scroll_to_instagram_video(browser_top_sites)
        pause_or_play_video_by_javascript(browser_top_sites, InstagramLocators.FIRST_VIDEO_HOME_PAGE_CSS)
        LOGGER.info("Check download video on homepage " + TopSitesUrls.INSTAGRAM_URL)
        video_title_root = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        video_title_temp = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(
            video_title_root)
        video_title = self.top_sites_savior_title_action.get_first_part_of_video_title(video_title_temp)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, SocialNetworkVideoLengthLocators.INSTAGRAM_VIDEO_HOMEPAGE_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

        browser_top_sites.get(TopSitesUrls.INSTAGRAM_VIDEO_URL)
        LOGGER.info("Check download video on " + TopSitesUrls.INSTAGRAM_VIDEO_URL)
        pause_or_play_video_by_javascript(browser_top_sites, InstagramLocators.FIRST_VIDEO_HOME_PAGE_CSS)
        video_title_root = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        video_title_temp = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(
            video_title_root)
        video_title = self.top_sites_savior_title_action.get_first_part_of_video_title(video_title_temp)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, SocialNetworkVideoLengthLocators.INSTAGRAM_VIDEO_OTHERS_PAGE_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

    # @pytestrail.case('C96721')
    # @pytest.mark.ten_popular_sites
    # @pytestrail.defect('PF-1219')
    # def test_download_file_phim_moi(self, browser, get_current_download_folder):
    #                                 #, clear_download_page ,):
    #     self.prepare_displayed_savior_popup(browser)
    #     video_title_start_with = self.top_sites_savior_title_actions.get_phimmoi_video_title(browser)
    #     try:
    #         implement_download_file(browser, get_current_download_folder, start_with=video_title_start_with)
    #     finally:
    #         delete_all_mp4_file_download(get_current_download_folder, '.mp4', star_with=video_title_start_with)
# import logging
# import time
# import pytest
# from pytest_testrail.plugin import pytestrail
# from models.pagelocators.top_savior_sites.top_savior_sites_social import FacebookLocators, InstagramLocators
# from models.pagelocators.top_savior_sites.top_savior_sites_video_length import TopSaviorSitesVideoLengthLocators, \
#     SocialNetworkVideoLengthLocators
# from models.pageobject.sites import AnySitePageObject
# from models.pageobject.top_savior_sites.top_savior_sites_film import TopSaviorSitesFilmActions
# from models.pageobject.top_savior_sites.top_savior_sites_social import FacebookActions, InstagramActions
# from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
# from models.pageobject.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthActions
# from testscripts.savior_top_100_sites.test_download_social_network import top_sites_savior_title_actions
# from utils_automation.const import VideoUrls, OtherSiteUrls
# from testscripts.savior_top_100_sites.common import download_and_verify_video, choose_highest_resolution_of_video, \
#     login_facebook, login_instagram
# from testscripts.common_setup import assert_file_download_value, delete_all_mp4_file_download, \
#     download_file_via_main_download_button, get_resolution_info, pause_or_play_video_by_javascript
#
# LOGGER = logging.getLogger(__name__)
# any_site_page_object = AnySitePageObject()
# top_sites_savior_title_action = TopSitesSaviorTitleAction()
# top_savior_sites_film_action = TopSaviorSitesFilmActions()
# top_savior_sites_video_length_action = TopSitesSaviorVideoLengthActions()
#
#
# class TestFilm:
#     @pytestrail.case('C98735')
#     @pytest.mark.ten_popular_sites
#     def test_download_dongphim(self, browser_top_sites, get_current_download_folder_top_sites):
#         browser_top_sites.get(VideoUrls.DONG_PHIM_VIDEO_URL)
#         LOGGER.info("Check download video on " + VideoUrls.DONG_PHIM_VIDEO_URL)
#         elements = any_site_page_object.choose_watch_option_if_any(browser_top_sites)
#         if len(elements) == 0:
#             any_site_page_object.click_video_item_dong_phim(browser_top_sites)
#         video_title = top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
#         expect_length = top_savior_sites_video_length_action. \
#             get_video_length(browser_top_sites,
#                              TopSaviorSitesVideoLengthLocators.DONG_PHYM_VIDEO_LENGTH_CSS)
#         download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)
#
#     @pytestrail.case('C98756')
#     def test_download_file_film_mot_phim_net(self, browser_top_sites, get_current_download_folder_top_sites):
#         browser_top_sites.get(OtherSiteUrls.MOT_PHIM_VIDEO_URL)
#         LOGGER.info("Check download video on " + OtherSiteUrls.MOT_PHIM_VIDEO_URL)
#         any_site_page_object.mouse_over_then_click_play_video_mot_phimzz(browser_top_sites)
#         choose_highest_resolution_of_video(browser_top_sites)
#         video_title_temp = top_sites_savior_title_action.get_video_title_from_span_tag(browser_top_sites)
#         video_title = top_sites_savior_title_action.replace_special_characters_by_dash_in_string(video_title_temp)
#         any_site_page_object.switch_to_video_iframe_mot_phimzz(browser_top_sites)
#         expect_length = top_savior_sites_video_length_action. \
#             get_video_length(browser_top_sites, TopSaviorSitesVideoLengthLocators.MOT_PHIMZZ_VIDEO_LENGTH)
#         browser_top_sites.switch_to.default_content()
#         media_info = download_file_via_main_download_button(browser_top_sites, video_title)
#         resolution_info = get_resolution_info(media_info)
#         try:
#             assert_file_download_value(get_current_download_folder_top_sites, resolution_info,
#                                        expect_length, start_with=video_title, end_with=".mp4")
#         finally:
#             delete_all_mp4_file_download(get_current_download_folder_top_sites, end_with=".mp4", start_with=video_title)
#
#
#
