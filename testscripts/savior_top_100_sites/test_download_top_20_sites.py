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
