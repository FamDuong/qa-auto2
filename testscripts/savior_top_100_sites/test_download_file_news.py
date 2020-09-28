import logging
import pytest

from models.pagelocators.sites import AnySite
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail

from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from testscripts.savior_top_100_sites.common import download_and_verify_video
from utils_automation.const import OtherSiteUrls

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()
top_site_titles_action = TopSitesSaviorTitleAction()

LOGGER = logging.getLogger(__name__)


class Test24H:

    @pytestrail.case('C96720')
    @pytest.mark.one_hundred_popular_sites
    def test_download_file_24h(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.NEWS_24H_BONGDA_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.NEWS_24H_BONGDA_URL)
        video_title_bong_da = top_site_titles_action.get_video_title_from_link(browser_top_sites,
                                                                               AnySite.NEWS_24H_VIDEO_TO_GET_TITLE_CSS,
                                                                               AnySite.NEWS_24H_VIDEO_TO_GET_TITLE)
        any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title_bong_da)

        browser_top_sites.get(OtherSiteUrls.NEWS_24H_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.NEWS_24H_URL)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)


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


class TestTuoiTre:

    @pytestrail.case('C98754')
    @pytest.mark.one_hundred_popular_sites
    def test_download_file_video_tuoi_tre(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.TUOI_TRE_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.TUOI_TRE_VIDEO_URL)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)


class TestVTCVN:

    @pytestrail.case('C98764')
    @pytest.mark.one_hundred_popular_sites
    def test_download_file_vtc_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.VTC_VN_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.VTC_VN_VIDEO_URL)
        any_site_page_object.click_video_element_vtc_v(browser_top_sites)
        video_title = top_site_titles_action.get_vtc_video_title(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)


class TestKenh14VN:

    @pytestrail.case('C98765')
    @pytest.mark.one_hundred_popular_sites
    def test_download_file_kenh14_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.KENH14_VN_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.KENH14_VN_VIDEO_URL)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)


class TestVNExpressNet:

    @pytestrail.case('C98772')
    @pytest.mark.one_hundred_popular_sites
    def test_download_file_vnexpress(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.VIDEO_VNEXPRESS_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.VIDEO_VNEXPRESS_URL)
        video_title = top_site_titles_action.get_video_vnexpress_video_title(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

        browser_top_sites.get(OtherSiteUrls.NEWS_VNEXPRESS_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.NEWS_VNEXPRESS_URL)
        any_site_page_object.scroll_to_news_video_vnexpress_video(browser_top_sites)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)


class TestThanhNienVN:
    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.THANH_NIEN_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.THANH_NIEN_VIDEO_URL)
        video_title_temp = top_site_titles_action.get_website_title_by_javascript(browser)
        video_title = top_site_titles_action.replace_vertical_bar_and_colon_by_dash_in_string(video_title_temp)
        return video_title

    @pytestrail.case('C98773')
    @pytest.mark.one_hundred_popular_sites
    def test_download_file_thanh_nien_viet_nam(self, browser_top_sites, get_current_download_folder_top_sites):
        video_title = self.prepare_savior_option_appear(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)


class TestDanTriVN:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.DAN_TRI_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.DAN_TRI_VIDEO_URL)
        video_title_temp = top_site_titles_action.get_website_title_by_javascript(browser)
        video_title = top_site_titles_action.replace_vertical_bar_and_colon_by_dash_in_string(video_title_temp)
        any_site_page_object.click_play_video_dan_tri_vn(browser)
        any_site_page_object.mouse_over_video_dan_tri_vn(browser)
        return video_title

    @pytestrail.case('C98775')
    @pytest.mark.one_hundred_popular_sites
    def test_download_file_dan_tri_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        video_title = self.prepare_savior_option_appear(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites,
                                  video_title, mouse_over_first_video=False)


class TestVtvGoVN:
    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.VTV_GO_VN_VIDEO_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.VTV_GO_VN_VIDEO_URL)
        video_title_temp = top_site_titles_action.get_website_title_by_javascript(browser)
        video_title = top_site_titles_action.replace_vertical_bar_and_colon_by_dash_in_string(video_title_temp)
        return video_title

    @pytestrail.case('C98796')
    @pytest.mark.one_hundred_popular_sites
    def test_download_vtv_go_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        video_title = self.prepare_savior_option_appear(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)
