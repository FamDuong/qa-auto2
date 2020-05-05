import pytest
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail

from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from testscripts.common_setup import implement_download_file, delete_all_mp4_file_download
from utils_automation.const import OtherSiteUrls

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()
top_sites_savior_title_actions = TopSitesSaviorTitleAction()


class TestFacebook:

    @pytestrail.case('C96691')
    @pytest.mark.ten_popular_sites
    @pytestrail.defect('PF-530')
    def test_download_file_facebook(self, browser_top_sites, get_current_download_folder_top_sites
                                    , clear_download_page):
        browser_top_sites.get(OtherSiteUrls.FACEBOOK_VIDEO_URL)
        video_title_start_with = top_sites_savior_title_actions.get_facebook_video_title(browser_top_sites)[0:7]
        any_site_page_object.mouse_over_video_element_facebook(browser_top_sites)
        try:
            implement_download_file(browser_top_sites, get_current_download_folder_top_sites)
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title_start_with)


class TestMessenger:

    def login_to_messenger_if_neccessary(self, driver):
        from models.pageobject.top_savior_sites.top_savior_sites_social import MessengerActions
        messenger_action = MessengerActions()
        len_login_elements = messenger_action.get_number_of_login_elements(driver=driver)
        if len_login_elements == 0:
            pass
        elif len_login_elements > 0:
            messenger_action.login_messenger_task(driver, email_or_phone_info='0838069260', password_info='Cuong1990#')

    def setup_savior_option_appear(self, driver):
        driver.get(OtherSiteUrls.MESSENGER_CHAT_URL)
        self.login_to_messenger_if_neccessary(driver)
        any_site_page_object.click_video_element_messenger_chat(driver)
        any_site_page_object.mouse_over_video_element_messenger_chat(driver)

    @pytestrail.case('C96722')
    def test_download_file_messenger(self, browser_top_sites, get_current_download_folder_top_sites
                                     , clear_download_page):
        self.setup_savior_option_appear(browser_top_sites)
        video_title_start_with = top_sites_savior_title_actions.get_messenger_video_title(browser_top_sites)
        try:
            implement_download_file(browser_top_sites, get_current_download_folder_top_sites, startwith=video_title_start_with),
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title_start_with)


class TestInstagram:

    @staticmethod
    def prepare_appear_savior_option(browser):
        browser.get(OtherSiteUrls.INSTAGRAM_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_instagram(browser)

    @pytestrail.case('C96751')
    @pytest.mark.ten_popular_sites
    def test_download_file_instagram(self, browser_top_sites, get_current_download_folder_top_sites
                                     , clear_download_page):
        self.prepare_appear_savior_option(browser_top_sites)
        from textwrap import wrap
        video_title_start_with = wrap(top_sites_savior_title_actions.get_instagram_video_title(browser_top_sites), 6)[0]
        try:
            implement_download_file(browser_top_sites, get_current_download_folder_top_sites, startwith=video_title_start_with),
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title_start_with)


class TestTwitter:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.TWITTER_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_twitter(browser)

    @pytestrail.case('C98721')
    def test_download_file_twitter(self, browser, get_current_download_folder
                                   , clear_download_page):
        self.prepare_savior_option_appear(browser)
        implement_download_file(browser, get_current_download_folder),


class TestWeibo:

    @pytestrail.case('C98802')
    def test_download_file_weibo(self, browser, get_current_download_folder
                                 , clear_download_page):
        browser.get(OtherSiteUrls.WEIBO_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_weibo(browser)
        implement_download_file(browser, get_current_download_folder),


class TestOkRu:

    @pytestrail.case('C204280')
    @pytest.mark.one_hundred_popular_sites
    def test_download_ok_ru(self, browser_top_sites, get_current_download_folder_top_sites, clear_download_page):
        browser_top_sites.get(OtherSiteUrls.OK_RU)
        video_title = top_sites_savior_title_actions.get_ok_ru_video_title(browser_top_sites)
        delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title)
        try:
            any_site_page_object.mouse_over_video_ok_ru(browser_top_sites)
            implement_download_file(browser_top_sites, get_current_download_folder_top_sites, time_sleep=10, file_size=0.42,
                                    startwith=video_title)
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title)
