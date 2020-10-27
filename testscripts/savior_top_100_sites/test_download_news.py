import logging
import time

import pytest

from models.pagelocators.sites import AnySite
from models.pagelocators.top_savior_sites.top_savior_sites_video_length import NewsVideoLengthLocators
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail

from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from models.pageobject.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthActions
from testscripts.common_setup import pause_any_video_site, pause_or_play_video_by_javascript
from testscripts.savior_top_100_sites.common import download_and_verify_video
from utils_automation.const import OtherSiteUrls, VideoUrls

LOGGER = logging.getLogger(__name__)


class TestNews:
    top_savior_sites_video_length_action = TopSitesSaviorVideoLengthActions()
    any_site_page_object = AnySitePageObject()
    savior_page_object = SaviorPageObject()
    top_site_titles_action = TopSitesSaviorTitleAction()

    @pytestrail.case('C96720')
    @pytest.mark.others
    def test_download_file_24h(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.NEWS_24H_BONGDA_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.NEWS_24H_BONGDA_URL)
        video_title_bong_da = self.top_site_titles_action.\
            get_video_title_from_link(browser_top_sites, AnySite.NEWS_24H_VIDEO_TO_GET_TITLE_CSS,
                                      AnySite.NEWS_24H_VIDEO_TO_GET_TITLE)
        pause_or_play_video_by_javascript(browser_top_sites, NewsVideoLengthLocators.NEWS_24H_BONGDA_VIDEO_CSS)
        expect_length_root = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, NewsVideoLengthLocators.NEWS_24H_BONGDA_VIDEO_CSS)
        expect_length = self.top_savior_sites_video_length_action.\
            get_video_length_after_span_tag(browser_top_sites, expect_length_root)
        self.any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length,
                                  video_title_bong_da)

        browser_top_sites.get(OtherSiteUrls.NEWS_24H_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.NEWS_24H_URL)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        pause_or_play_video_by_javascript(browser_top_sites, NewsVideoLengthLocators.NEWS_24H_BONGDA_VIDEO_CSS)
        expect_length_root = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, NewsVideoLengthLocators.NEWS_24H_BONGDA_VIDEO_CSS)
        expect_length = self.top_savior_sites_video_length_action.\
            get_video_length_after_span_tag(browser_top_sites, expect_length_root)

        self.any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

    # Still error
    # class TestVietnamNet:
    #
    #     @staticmethod
    #     def prepare_savior_option_displayed(browser):
    #         browser.get(OtherSiteUrls.VIETNAMNET_VIDEO_URL)
    #         any_site_page_object.mouse_over_video_item_vietnamnet(browser)
    #
    #     @pytestrail.case('C96759')
    #     def test_download_file_vietnamnet(self, browser_top_sites, get_current_download_folder_top_sites):
    #         browser_top_sites.get(OtherSiteUrls.VIETNAMNET_VIDEO_URL)
    #         LOGGER.info("Check download video on " + OtherSiteUrls.VIETNAMNET_VIDEO_URL)
    #         video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
    #         any_site_page_object.mouse_over_video_item_vietnamnet(browser_top_sites)
    #         download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title,
    #                                   mouse_over_first_video=False)
    # self.prepare_savior_option_displayed(browser_top_sites)
    # verify_download_quality_high_frame(browser_top_sites, get_current_download_folder_top_sites,
    #                                    self.prepare_savior_option_displayed),

    @pytestrail.case('C98754')
    @pytest.mark.others
    def test_download_file_video_tuoi_tre(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.TUOI_TRE_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.TUOI_TRE_VIDEO_URL)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length=0, video_title=video_title)

    @pytestrail.case('C98764')
    @pytest.mark.others
    def test_download_file_vtc_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.VTC_VN_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.VTC_VN_VIDEO_URL)
        video_title_root = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        video_title_temp = self.top_site_titles_action.replace_special_characters_by_dash_in_string(video_title_root)
        video_title = self.top_site_titles_action.get_first_part_of_video_title(video_title_temp)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length=0, video_title=video_title)

    @pytestrail.case('C98765')
    @pytest.mark.others
    def test_download_file_kenh14_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.KENH14_VN_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.KENH14_VN_VIDEO_URL)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length=0, video_title=video_title)

    @pytestrail.case('C98772')
    @pytest.mark.others
    def test_download_file_vnexpress(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.VIDEO_VNEXPRESS_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.VIDEO_VNEXPRESS_URL)
        video_title = self.top_site_titles_action.get_video_vnexpress_video_title(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length=0, video_title=video_title)

        browser_top_sites.get(OtherSiteUrls.NEWS_VNEXPRESS_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.NEWS_VNEXPRESS_URL)
        self.any_site_page_object.scroll_to_news_video_vnexpress_video(browser_top_sites)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length=0, video_title=video_title)

    def prepare_savior_option_appear_thanh_nien(self, browser):
        browser.get(OtherSiteUrls.THANH_NIEN_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.THANH_NIEN_VIDEO_URL)
        video_title_temp = self.top_site_titles_action.get_website_title_by_javascript(browser)
        video_title = self.top_site_titles_action.replace_special_characters_by_dash_in_string(video_title_temp)
        return video_title

    @pytestrail.case('C98773')
    @pytest.mark.others
    def test_download_file_thanh_nien_viet_nam(self, browser_top_sites, get_current_download_folder_top_sites):
        video_title = self.prepare_savior_option_appear_thanh_nien(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length=0, video_title=video_title)

    def prepare_savior_option_appear_dan_tri(self, browser):
        browser.get(OtherSiteUrls.DAN_TRI_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.DAN_TRI_VIDEO_URL)
        video_title_temp = self.top_site_titles_action.get_website_title_by_javascript(browser)
        video_title = self.top_site_titles_action.replace_special_characters_by_dash_in_string(video_title_temp)
        self.any_site_page_object.click_play_video_dan_tri_vn(browser)
        self.any_site_page_object.mouse_over_video_dan_tri_vn(browser)
        return video_title

    @pytestrail.case('C98775')
    @pytest.mark.others
    def test_download_file_dan_tri_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        video_title = self.prepare_savior_option_appear_dan_tri(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  expect_length=0, video_title=video_title, mouse_over_first_video=False)

    def prepare_savior_option_appear_vtv_go(self, browser):
        browser.get(OtherSiteUrls.VTV_GO_VN_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.VTV_GO_VN_VIDEO_URL)
        video_title_temp = self.top_site_titles_action.get_website_title_by_javascript(browser)
        video_title = self.top_site_titles_action.replace_special_characters_by_dash_in_string(video_title_temp)
        return video_title

    @pytestrail.case('C98796')
    @pytest.mark.others
    def test_download_vtv_go_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        video_title = self.prepare_savior_option_appear_vtv_go(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length=0, video_title=video_title)

    @pytestrail.case('C96752')
    @pytest.mark.others
    def test_download_news_zing(self, browser_top_sites, get_current_download_folder_top_sites):
        pause_any_video_site(browser_top_sites, VideoUrls.NEWS_ZING_VIDEO_URL)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length=0, video_title=video_title)
