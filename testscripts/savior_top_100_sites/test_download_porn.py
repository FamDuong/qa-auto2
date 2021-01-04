import logging

import pytest
from pytest_testrail.plugin import pytestrail

from models.pagelocators.top_savior_sites.top_savior_sites_video_length import OnlinePornVideoLengthLocators
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from models.pageobject.top_savior_sites.top_savior_sites_video_length import TopSitesSaviorVideoLengthActions
from testscripts.common_setup import implement_download_file, download_file_via_main_download_button, \
    get_resolution_info, assert_file_download_value, delete_all_mp4_file_download, pause_or_play_video_by_javascript
from testscripts.savior_top_100_sites.common import download_and_verify_video
from utils_automation.const import OtherSiteUrls, OnlinePornUrls
from utils_automation.setup import WaitAfterEach

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()
top_sites_savior_title_action = TopSitesSaviorTitleAction()
LOGGER = logging.getLogger(__name__)


class TestOnlinePorn:
    top_sites_savior_title_action = TopSitesSaviorTitleAction()
    top_savior_sites_video_length_action = TopSitesSaviorVideoLengthActions()
    any_site_page_object = AnySitePageObject()

    @pytestrail.case('C98771')
    @pytest.mark.top_sites
    def test_download_fr_porn_hub(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OnlinePornUrls.FR_PORN_HUB_URL)
        LOGGER.info("Check download music on " + OnlinePornUrls.FR_PORN_HUB_URL)
        video_title_root = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        video_title = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(video_title_root)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, OnlinePornVideoLengthLocators.FR_PORN_HUB_VIDEO_CSS)
        pause_or_play_video_by_javascript(browser_top_sites, OnlinePornVideoLengthLocators.FR_PORN_HUB_VIDEO_CSS)
        self.any_site_page_object.mouse_over_video_fr_porn_hub(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length,
                                  video_title, mouse_over_first_video=False)

    @pytestrail.case('C410748')
    @pytest.mark.top_sites
    def test_download_xhamster_one(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OnlinePornUrls.XHAMSTER_ONE_URL)
        LOGGER.info("Check download music on " + OnlinePornUrls.XHAMSTER_ONE_URL)
        video_title_root = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        video_title = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(video_title_root)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, OnlinePornVideoLengthLocators.XHAMSTER_ONE_VIDEO_LENGHT_CSS)
        self.any_site_page_object.click_play_video_xhamster_one(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

    @pytestrail.case('C410751')
    @pytest.mark.top_sites
    def test_download_thumbzilla(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OnlinePornUrls.THUMBZILLA_URL)
        LOGGER.info("Check download music on " + OnlinePornUrls.THUMBZILLA_URL)
        video_title_root = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
        video_title = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(video_title_root)
        expect_length = self.top_savior_sites_video_length_action. \
            get_video_length(browser_top_sites, OnlinePornVideoLengthLocators.THUMBZILLA_VIDEO_LENGHT_CSS)
        pause_or_play_video_by_javascript(browser_top_sites, OnlinePornVideoLengthLocators.THUMBZILLA_VIDEO_LENGHT_CSS)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)

    # @pytestrail.case('C410754')
    # @pytest.mark.top_sites
    # def test_download_fr_spankbang(self, browser_top_sites, get_current_download_folder_top_sites):
    #     browser_top_sites.get(OnlinePornUrls.FR_SPANKBANG_URL)
    #     LOGGER.info("Check download music on " + OnlinePornUrls.FR_SPANKBANG_URL)
    #     video_title_root = self.top_sites_savior_title_action.get_website_title_by_javascript(browser_top_sites)
    #     video_title = self.top_sites_savior_title_action.replace_special_characters_by_dash_in_string(video_title_root)
    #     expect_length = self.top_savior_sites_video_length_action. \
    #         get_video_length(browser_top_sites, OnlinePornVideoLengthLocators.FR_SPANKBANG_VIDEO_LENGHT_CSS)
    #     pause_or_play_video_by_javascript(browser_top_sites, OnlinePornVideoLengthLocators.FR_SPANKBANG_VIDEO_LENGHT_CSS)
    #     download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, expect_length, video_title)


class TestXVideos:

    @pytestrail.case('C162034')
    @pytestrail.defect('PF-859')
    @pytest.mark.ten_popular_sites
    def test_download_file_x_videos(self, browser_top_sites, get_current_download_folder_top_sites,
                                    clear_download_page):
        browser_top_sites.get(OtherSiteUrls.XVIDEOS_DOT_COM_VIDEO_URL)
        title = top_sites_savior_title_action.get_x_videos_title_video(browser_top_sites)[0:4]
        try:
            any_site_page_object.click_video_x_videos(browser_top_sites)
            any_site_page_object.mouse_over_video_x_videos(browser_top_sites)
            implement_download_file(browser_top_sites, get_current_download_folder_top_sites, startwith=title)
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=title)


class TestXNXX:

    @pytestrail.case('C162037')
    @pytestrail.defect('PF-833')
    @pytest.mark.ten_popular_sites
    def test_download_file_xnxx_videos(self, browser_top_sites, get_current_download_folder_top_sites
                                       , clear_download_page):
        browser_top_sites.get(OtherSiteUrls.XNXX_VIDEO_URL)
        title = top_sites_savior_title_action.get_xnxx_video_title(browser_top_sites)
        try:
            any_site_page_object.click_play_video_item_xnxx(browser_top_sites)
            any_site_page_object.mouse_over_video_xnxx(browser_top_sites)
            implement_download_file(browser_top_sites, get_current_download_folder_top_sites, startwith=title),
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=title)


# class TestPornHub:
#
#     @pytestrail.case('C204205')
#     @pytestrail.defect('PF-620')
#     @pytest.mark.ten_popular_sites
#     def test_download_file_porn_hub(self, browser_top_sites, get_current_download_folder_top_sites
#                                     , clear_download_page, ):
#         browser_top_sites.get(OtherSiteUrls.FR_PORN_HUB_VIDEO_URL)
#         title = top_sites_savior_title_action.get_fr_pornhub_video_title(browser_top_sites)
#         any_site_page_object.click_video_fr_porn_hub(browser_top_sites)
#         any_site_page_object.mouse_over_video_fr_porn_hub(browser_top_sites)
#         try:
#             implement_download_file(browser_top_sites, get_current_download_folder_top_sites, time_sleep=10)
#         finally:
#             delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=title)


class TestVLXX:

    @pytestrail.case('C96762')
    def test_download_file_vlxx_videos(self, browser, get_current_download_folder
                                       , clear_download_page):
        browser.get(OtherSiteUrls.VLXX_VIDEO_URL)
        any_site_page_object.click_video_vlxx(browser)
        any_site_page_object.mouse_over_video_vlxx(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestSexTop1:

    @pytestrail.case('C98726')
    def test_download_file_sex_top1_video(self, browser, get_current_download_folder
                                          , clear_download_page):
        browser.get(OtherSiteUrls.SEX_TOP1_VIDEO_URL)
        any_site_page_object.click_video_sex_top1(browser)
        any_site_page_object.mouse_over_video_sex_top1(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestSexHiHi:

    @pytestrail.case('C98731')
    def test_download_file_sex_hihi_video(self, browser, get_current_download_folder
                                          , clear_download_page):
        browser.get(OtherSiteUrls.SEX_HIHI_VIDEO_URL)
        WaitAfterEach.sleep_timer_after_each_step()
        any_site_page_object.click_video_sex_hihi(browser)
        any_site_page_object.mouse_over_video_sex_hihi(browser)
        implement_download_file(browser, get_current_download_folder, )


class TestJavHdPro:

    @pytestrail.case('C98744')
    def test_download_file_jav_hd_pro(self, browser, get_current_download_folder
                                      , clear_download_page):
        browser.get(OtherSiteUrls.JAV_HD_PRO_VIDEO_URL)
        any_site_page_object.click_video_jav_hd_pro(browser)
        any_site_page_object.mouse_over_video_jav_hd_pro(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestPhimSexPorn:

    @pytestrail.case('C98774')
    @pytest.mark.last
    def test_download_file_phim_sex_porn(self, browser, get_current_download_folder
                                         , clear_download_page):
        browser.get(OtherSiteUrls.PHIM_SEX_PORN_VIDEO_URL)
        any_site_page_object.switch_to_iframe_phim_sex_porn(browser)
        any_site_page_object.click_video_phim_sex_porn(browser)
        browser.switch_to.default_content()
        any_site_page_object.mouse_over_video_phim_sex_porn(browser)
        implement_download_file(browser, get_current_download_folder),


class TestJavPhim:

    @pytestrail.case('C98783')
    def test_download_file_jav_phim(self, browser, get_current_download_folder
                                    , clear_download_page):
        browser.get(OtherSiteUrls.JAV_PHIM_VIDEO_URL)
        any_site_page_object.click_video_jav_phim(browser)
        any_site_page_object.mouse_over_video_jav_phim(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestSexNgon:

    @pytestrail.case('C98799')
    def test_download_file_sex_ngon(self, browser, get_current_download_folder
                                    , clear_download_page):
        browser.get(OtherSiteUrls.SEX_NGON_VIDEO_URL)
        any_site_page_object.click_video_element_sex_ngon(browser)
        any_site_page_object.mouse_over_video_element_sex_ngon(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestPhimSexSub:

    @pytestrail.case('C98806')
    def test_download_file_phim_sex_sub(self, browser, get_current_download_folder
                                        , clear_download_page):
        browser.get(OtherSiteUrls.PHIM_SEX_SUB_VIDEO_URL)
        any_site_page_object.click_video_phim_sex_sub_video_element(browser)
        any_site_page_object.mouse_over_video_element_phim_sex_sub(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestHentaizNet:

    @pytestrail.case('C98729')
    def test_download_file_hentaiz_net(self, browser, get_current_download_folder
                                       , clear_download_page, choose_low_quality_option
                                       , revert_high_quality_default_option):
        browser.get(OtherSiteUrls.HENTAIZ_NET_VIDEO_URL)
        any_site_page_object.click_video_hentaiz_net(browser)
        any_site_page_object.mouse_over_video_hentaiz_net(browser)
        media_info = download_file_via_main_download_button(browser, )
        resolution_info = get_resolution_info(media_info)
        assert_file_download_value(get_current_download_folder, resolution_info)
