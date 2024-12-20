import logging
import time

import pytest

from models.pagelocators.top_savior_sites.top_savior_sites_social import InstagramLocators, FacebookLocators
from models.pagelocators.top_savior_sites.top_savior_sites_video_length import TopSaviorSitesVideoLengthLocators, \
    SocialNetworkVideoLengthLocators
# from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from models.pageobject.top_savior_sites.top_savior_sites_film import TopSaviorSitesFilmActions
from models.pageobject.top_savior_sites.top_savior_sites_social import FacebookActions, InstagramActions
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from models.pageobject.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthActions
from testscripts.common_setup import delete_all_mp4_file_download, \
    download_file_via_main_download_button, get_resolution_info, assert_file_download_value, \
    pause_or_play_video_by_javascript
from testscripts.savior_top_100_sites.common import download_and_verify_video, login_facebook, \
    choose_highest_resolution_of_video, login_instagram, verify_download_file_facebook_by_url
from utils_automation.const import OtherSiteUrls, SocialNetworkUrls

LOGGER = logging.getLogger(__name__)


class TestSocialNetwork:
    facebook_action = FacebookActions()
    instagram_action = InstagramActions()
    any_site_page_object = AnySitePageObject()
    top_sites_savior_title_action = TopSitesSaviorTitleAction()
    top_savior_sites_film_action = TopSaviorSitesFilmActions()
    top_savior_sites_video_length_action = TopSitesSaviorVideoLengthActions()

    @pytestrail.case('C96691')
    @pytestrail.defect('PF-530')
    @pytest.mark.top_sites
    def test_download_file_facebook(self, browser_top_sites, get_current_download_folder_top_sites):
        verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
                                             SocialNetworkUrls.FACEBOOK_HOMEPAGE_URL)
        verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
                                             SocialNetworkUrls.FACEBOOK_PROFILE_ME_URL)
        verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
                                             SocialNetworkUrls.FACEBOOK_PROFILE_NGOCTRINH_URL)
        verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
                                            SocialNetworkUrls.FACEBOOK_WATCH_URL)
        verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
                                             SocialNetworkUrls.FACEBOOK_VIDEO_URL)
        verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
                                            SocialNetworkUrls.FACEBOOK_VTVGIAITRI_PAGE_URL)
        verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
                                             SocialNetworkUrls.FACEBOOK_GROUP_URL)
        verify_download_file_facebook_by_url(browser_top_sites, get_current_download_folder_top_sites,
                                             SocialNetworkUrls.FACEBOOK_WATCH_URL, need_opened_video=True)


    @pytestrail.case('C204280')
    @pytest.mark.top_sites
    def test_download_ok_ru(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(SocialNetworkUrls.OK_RU)
        LOGGER.info("Check download video on " + SocialNetworkUrls.OK_RU)
        video_title = self.top_sites_savior_title_action.get_ok_ru_video_title(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites,
                             TopSaviorSitesVideoLengthLocators.OK_RU_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

        # def prepare_appear_savior_option(self, browser):
        #     browser.get(TopSitesUrls.INSTAGRAM_VIDEO_URL)
        #     self.any_site_page_object.mouse_over_video_element_instagram(browser)

    @pytestrail.case('C96751')
    @pytestrail.defect('PF-2078')
    @pytest.mark.top_sites
    def test_download_file_instagram(self, browser_top_sites, get_current_download_folder_top_sites):
        login_instagram(browser_top_sites)
        browser_top_sites.get(SocialNetworkUrls.INSTAGRAM_URL)
        LOGGER.info("Check download video on " + SocialNetworkUrls.INSTAGRAM_URL)
        self.instagram_action.scroll_to_instagram_video(browser_top_sites)
        pause_or_play_video_by_javascript(browser_top_sites, InstagramLocators.FIRST_VIDEO_HOME_PAGE_CSS)
        LOGGER.info("Check download video on homepage " + SocialNetworkUrls.INSTAGRAM_URL)
        video_title_root = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        video_title_temp = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(
            video_title_root)
        video_title = self.top_sites_savior_title_action.get_first_part_of_video_title(video_title_temp)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, SocialNetworkVideoLengthLocators.INSTAGRAM_VIDEO_HOMEPAGE_CSS,
                             element="", url=SocialNetworkUrls.INSTAGRAM_URL)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

        browser_top_sites.get(SocialNetworkUrls.INSTAGRAM_VIDEO_URL)
        LOGGER.info("Check download video on " + SocialNetworkUrls.INSTAGRAM_VIDEO_URL)
        pause_or_play_video_by_javascript(browser_top_sites, InstagramLocators.FIRST_VIDEO_HOME_PAGE_CSS)
        video_title_root = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        video_title_temp = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(
            video_title_root)
        video_title = self.top_sites_savior_title_action.get_first_part_of_video_title(video_title_temp)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, SocialNetworkVideoLengthLocators.INSTAGRAM_VIDEO_OTHERS_PAGE_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

# class TestMessenger:
#
#     def login_to_messenger_if_neccessary(self, driver):
#         from models.pageobject.top_savior_sites.top_savior_sites_social import MessengerActions
#         messenger_action = MessengerActions()
#         len_login_elements = messenger_action.get_number_of_login_elements(driver=driver)
#         if len_login_elements == 0:
#             pass
#         elif len_login_elements > 0:
#             messenger_action.login_messenger_task(driver, email_or_phone_info='0838069260', password_info='Cuong1990#')
#
#     def setup_savior_option_appear(self, driver):
#         driver.get(OtherSiteUrls.MESSENGER_CHAT_URL)
#         self.login_to_messenger_if_neccessary(driver)
#         any_site_page_object.click_video_element_messenger_chat(driver)
#         any_site_page_object.mouse_over_video_element_messenger_chat(driver)
#
#     @pytestrail.case('C96722')
#     def test_download_file_messenger(self, browser_top_sites, get_current_download_folder_top_sites
#                                      , clear_download_page):
#         self.setup_savior_option_appear(browser_top_sites)
#         video_title_start_with = top_sites_savior_title_actions.get_messenger_video_title(browser_top_sites)
#         try:
#             implement_download_file(browser_top_sites, get_current_download_folder_top_sites, startwith=video_title_start_with),
#         finally:
#             delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title_start_with)
#
#
# class TestTwitter:
#
#     @staticmethod
#     def prepare_savior_option_appear(browser):
#         browser.get(OtherSiteUrls.TWITTER_VIDEO_URL)
#         any_site_page_object.mouse_over_video_item_twitter(browser)
#
#     @pytestrail.case('C98721')
#     def test_download_file_twitter(self, browser, get_current_download_folder
#                                    , clear_download_page):
#         self.prepare_savior_option_appear(browser)
#         implement_download_file(browser, get_current_download_folder),
#
#
# class TestWeibo:
#
#     @pytestrail.case('C98802')
#     def test_download_file_weibo(self, browser, get_current_download_folder
#                                  , clear_download_page):
#         browser.get(OtherSiteUrls.WEIBO_VIDEO_URL)
#         any_site_page_object.mouse_over_video_element_weibo(browser)
#         implement_download_file(browser, get_current_download_folder),
