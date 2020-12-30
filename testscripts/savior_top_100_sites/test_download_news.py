import logging
import pytest

from models.pagelocators.sites import AnySite
from models.pagelocators.top_savior_sites.top_savior_sites_news import TopSaviorSitesNewsLocators
from models.pagelocators.top_savior_sites.top_savior_sites_video_length import NewsVideoLengthLocators
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from models.pageobject.top_savior_sites.top_savior_sites_news import TopSaviorSitesNewsActions
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from models.pageobject.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthActions
from testscripts.common_setup import pause_or_play_video_by_javascript
from testscripts.savior_top_100_sites.common import download_and_verify_video
from utils_automation.const import OtherSiteUrls, NewsUrls

LOGGER = logging.getLogger(__name__)


class TestNews:
    top_savior_sites_video_length_action = TopSitesSaviorVideoLengthActions()
    any_site_page_object = AnySitePageObject()
    savior_page_object = SaviorPageObject()
    top_site_titles_action = TopSitesSaviorTitleAction()
    top_savior_sites_news_action = TopSaviorSitesNewsActions()

    @pytestrail.case('C96720')
    @pytest.mark.others
    def test_download_file_24h(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(NewsUrls.NEWS_24H_BONGDA_URL)
        LOGGER.info("Check download video on " + NewsUrls.NEWS_24H_BONGDA_URL)
        video_title_bong_da = self.top_site_titles_action. \
            get_video_title_from_link(browser_top_sites, AnySite.NEWS_24H_VIDEO_TO_GET_TITLE_CSS,
                                      AnySite.NEWS_24H_VIDEO_TO_GET_TITLE)
        pause_or_play_video_by_javascript(browser_top_sites, NewsVideoLengthLocators.NEWS_24H_BONGDA_VIDEO_CSS)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, NewsVideoLengthLocators.NEWS_24H_BONGDA_VIDEO_CSS)
        self.any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length,
                                  video_title_bong_da)

        browser_top_sites.get(NewsUrls.NEWS_24H_URL)
        LOGGER.info("Check download video on " + NewsUrls.NEWS_24H_URL)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        pause_or_play_video_by_javascript(browser_top_sites, NewsVideoLengthLocators.NEWS_24H_BONGDA_VIDEO_CSS)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, NewsVideoLengthLocators.NEWS_24H_BONGDA_VIDEO_CSS)
        self.any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

    # def prepare_savior_option_displayed(self, browser):
    #     browser.get(NewsUrls.VIETNAMNET_VIDEO_URL)
    #     self.any_site_page_object.mouse_over_video_item_vietnamnet(browser)

    @pytestrail.case('C96759')
    @pytest.mark.others
    def test_download_file_vietnamnet(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(NewsUrls.VIETNAMNET_VIDEO_URL)
        LOGGER.info("Check download video on " + NewsUrls.VIETNAMNET_VIDEO_URL)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)

        self.top_savior_sites_news_action.switch_to_vietnamnet_video_iframe(
            browser_top_sites, TopSaviorSitesNewsLocators.VIETNAMNET_VIDEO_PARENT_IFRAME1)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesNewsLocators.VIETNAMNET_VIDEO_LENGTH_CSS)
        browser_top_sites.switch_to.default_content()
        # self.top_savior_sites_news_action.switch_to_vietnamnet_video_iframe(
        #     browser_top_sites, TopSaviorSitesNewsLocators.VIETNAMNET_VIDEO_PARENT_IFRAME2)
        self.any_site_page_object.mouse_over_video_iframe(driver=browser_top_sites)
        self.top_savior_sites_news_action.mouse_over_vietnamnet_video(browser_top_sites,
                                                                      TopSaviorSitesNewsLocators.VIETNAMNET_VIDEO)

        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  expect_length, video_title, mouse_over_first_video=False)
        self.prepare_savior_option_displayed(browser_top_sites)
        verify_download_quality_high_frame(browser_top_sites, get_current_download_folder_top_sites,
                                           self.prepare_savior_option_displayed),

    @pytestrail.case('C98754')
    @pytest.mark.others
    def test_download_file_video_tuoi_tre(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(NewsUrls.TUOI_TRE_VIDEO_URL)
        LOGGER.info("Check download video on " + NewsUrls.TUOI_TRE_VIDEO_URL)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesNewsLocators.TV_TUOITRE_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  expect_length, start_with=video_title)

    @pytestrail.case('C98765')
    @pytest.mark.others
    def test_download_file_kenh14_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(NewsUrls.KENH14_VN_VIDEO_URL)
        LOGGER.info("Check download video on " + NewsUrls.KENH14_VN_VIDEO_URL)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesNewsLocators.KENH14_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  expect_length, start_with=video_title)

    @pytestrail.case('C98772')
    @pytest.mark.others
    def test_download_file_vnexpress(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(NewsUrls.VIDEO_VNEXPRESS_URL)
        LOGGER.info("Check download video on " + NewsUrls.VIDEO_VNEXPRESS_URL)
        video_title = self.top_site_titles_action.get_video_vnexpress_video_title(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesNewsLocators.VNEXPRESS_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  expect_length, start_with=video_title)

        browser_top_sites.get(NewsUrls.NEWS_VNEXPRESS_URL)
        LOGGER.info("Check download video on " + NewsUrls.NEWS_VNEXPRESS_URL)
        self.any_site_page_object.scroll_to_news_video_vnexpress_video(browser_top_sites)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesNewsLocators.VNEXPRESS_NEWS_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  expect_length, start_with=video_title)

    @pytestrail.case('C98773')
    @pytest.mark.others
    def test_download_file_thanh_nien_viet_nam(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(NewsUrls.THANH_NIEN_VIDEO_URL)
        LOGGER.info("Check download video on " + NewsUrls.THANH_NIEN_VIDEO_URL)
        video_title_temp = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        video_title = self.top_site_titles_action.replace_special_characters_by_dash_in_string(video_title_temp)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesNewsLocators.THANH_NIEN_VIDEO_LENGTH_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  expect_length, start_with=video_title)

    @pytestrail.case('C98775')
    @pytest.mark.others
    def test_download_file_dan_tri_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(NewsUrls.DAN_TRI_VIDEO_URL)
        LOGGER.info("Check download video on " + NewsUrls.DAN_TRI_VIDEO_URL)
        video_title_temp = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        video_title = self.top_site_titles_action.replace_special_characters_by_dash_in_string(video_title_temp)
        self.any_site_page_object.click_play_video_dan_tri_vn(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesNewsLocators.DANTRI_VIDEO_LENGTH_CSS)
        self.any_site_page_object.mouse_over_video_dan_tri_vn(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  expect_length, start_with=video_title, mouse_over_first_video=False)

    @pytestrail.case('C98796')
    @pytest.mark.others
    def test_download_vtv_go_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.VTV_GO_VN_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.VTV_GO_VN_VIDEO_URL)
        video_title_temp = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        video_title = self.top_site_titles_action.replace_special_characters_by_dash_in_string(video_title_temp)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesNewsLocators.VTV_GO_VIDEO_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  expect_length, start_with=video_title)

    @pytestrail.case('C96752')
    @pytest.mark.others
    def test_download_news_zing(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(NewsUrls.NEWS_ZING_VIDEO_URL)
        LOGGER.info("Check download video on " + NewsUrls.NEWS_ZING_VIDEO_URL)
        video_title = self.top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        self.top_savior_sites_news_action.click_zing_news_play_video_button(browser_top_sites)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, TopSaviorSitesNewsLocators.ZINGNEWS_VIDEO_CSS)
        self.any_site_page_object.mouse_over_first_video_element(browser_top_sites,
                                                                 TopSaviorSitesNewsLocators.ZINGNEWS_VIDEO)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length,
                                  start_with=video_title, mouse_over_first_video=False)
