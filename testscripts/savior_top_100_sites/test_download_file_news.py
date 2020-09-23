import logging
import time

import pytest

from models.pagelocators.sites import AnySite
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail

from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from testscripts.common_setup import delete_all_mp4_file_download, \
    implement_download_file, verify_download_quality_high_frame, \
    choose_video_quality_medium_option, pause_or_play_video_by_javascript
from testscripts.savior_top_100_sites.common import download_and_verify_video
from utils_automation.const import OtherSiteUrls
from utils_automation.setup import WaitAfterEach
from models.pageobject.basepage_object import BasePageObject
any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()
top_site_titles_action = TopSitesSaviorTitleAction()

LOGGER = logging.getLogger(__name__)


class Test24H:

    # @staticmethod
    # def mouse_over_video_element_24h(browser):
    #     browser.get(OtherSiteUrls.NEWS_24H_URL)
    #     any_site_page_object.mouse_over_video_element_24h(browser)
    #
    # def prepare_check_download(self, browser, download_folder):
    #     self.mouse_over_video_element_24h(browser)
    #     delete_all_mp4_file_download(download_folder, '.mp4')
    #     WaitAfterEach.sleep_timer_after_each_step()

    @pytestrail.case('C96720')
    def test_download_file_24h(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.NEWS_24H_BONGDA_URL)
        video_title_bong_da = top_site_titles_action.get_video_title_from_link(browser_top_sites,
                                                                               AnySite.NEWS_24H_VIDEO_TO_GET_TITLE_CSS)
        any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title_bong_da)

        browser_top_sites.get(OtherSiteUrls.NEWS_24H_URL)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)


# Still error
class TestVietnamNet:

    @staticmethod
    def prepare_savior_option_displayed(browser):
        browser.get(OtherSiteUrls.VIETNAMNET_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_vietnamnet(browser)

    @pytestrail.case('C96759')
    def test_download_file_vietnamnet(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.VIETNAMNET_VIDEO_URL)

        any_site_page_object.swith_to_vietnamnet_video_iframe(browser_top_sites)
        any_site_page_object.mouse_over_video_item_vietnamnet(browser_top_sites)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)

        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title,
                                  mouse_over_first_video=False)
        # self.prepare_savior_option_displayed(browser_top_sites)
        # verify_download_quality_high_frame(browser_top_sites, get_current_download_folder_top_sites,
        #                                    self.prepare_savior_option_displayed),


class TestTuoiTre:

    @pytestrail.case('C98754')
    def test_download_file_video_tuoi_tre(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.TUOI_TRE_VIDEO_URL)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)


class TestVTCVN:

    @pytestrail.case('C98764')
    def test_download_file_vtc_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.VTC_VN_VIDEO_URL)
        any_site_page_object.click_video_element_vtc_v(browser_top_sites)
        video_title = top_site_titles_action.get_vtc_video_title(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)


class TestKenh14VN:

    @pytestrail.case('C98765')
    def test_download_file_kenh14_vn(self, browser_top_sites, get_current_download_folder_top_sites
                                     ):
        browser_top_sites.get(OtherSiteUrls.KENH14_VN_VIDEO_URL)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)


class TestVNExpressNet:
    base_page_object = BasePageObject()

    @pytestrail.case('C98772')
    def test_download_file_vnexpress(self, browser_top_sites, get_current_download_folder_top_sites):
        # browser_top_sites.get(OtherSiteUrls.VIDEO_VNEXPRESS_URL)
        # LOGGER.info("Check download video on "+OtherSiteUrls.VIDEO_VNEXPRESS_URL)
        # video_title = top_site_titles_action.get_video_vnexpress_video_title(browser_top_sites)
        # download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)

        browser_top_sites.get(OtherSiteUrls.NEWS_VNEXPRESS_URL)
        LOGGER.info("Check download video on " + OtherSiteUrls.NEWS_VNEXPRESS_URL)

        # self.base_page_object.scroll_to_with_scroll_height(browser_top_sites)
        # pause_or_play_video_by_javascript(browser_top_sites, action='play')
        any_site_page_object.mouse_over_video_vn_express(browser_top_sites)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        time.sleep(2)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title, mouse_over_first_video=False)


class TestThanhNienVN:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.THANH_NIEN_VIDEO_URL)
        any_site_page_object.click_video_thanh_nien_vn(browser)
        any_site_page_object.mouse_over_video_thanh_nien_vn(browser)

    @pytestrail.case('C98773')
    def test_download_file_thanh_nien_viet_nam(self, browser, get_current_download_folder
                                               , clear_download_page):
        self.prepare_savior_option_appear(browser)
        implement_download_file(browser, get_current_download_folder),


class TestDanTriVN:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.DAN_TRI_VIDEO_URL)
        any_site_page_object.click_play_video_dan_tri_vn(browser)
        any_site_page_object.mouse_over_video_dan_tri_vn(browser)

    @pytestrail.case('C98775')
    def test_download_file_dan_tri_vn(self, browser, get_current_download_folder
                                      , clear_download_page):
        self.prepare_savior_option_appear(browser)
        implement_download_file(browser, get_current_download_folder)


class TestNguoiLaoDongTV:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.NGUOI_LAO_DONG_TV_URL)
        any_site_page_object.click_video_nguoi_lao_dong_tv(browser)
        any_site_page_object.mouse_over_video_nguoi_lao_dong_tv(browser)

    @pytestrail.case('C98777')
    def test_download_file_nguoi_lao_dong_tv(self, browser, get_current_download_folder
                                             , clear_download_page):
        self.prepare_savior_option_appear(browser)
        implement_download_file(browser, get_current_download_folder),


class TestTinMoi:

    @pytestrail.case('C98784')
    def test_download_file_tin_moi(self, browser, get_current_download_folder
                                   , clear_download_page):
        browser.get(OtherSiteUrls.TIN_MOI_VIDEO_URL)
        any_site_page_object.mouse_over_video_tin_moi(browser)
        implement_download_file(browser, get_current_download_folder),


class TestInfoNet:

    @pytestrail.case('C98787')
    def test_download_file_info_net(self, browser, get_current_download_folder
                                    , clear_download_page):
        browser.get(OtherSiteUrls.INFO_NET_VIDEO_URL)
        any_site_page_object.click_video_info_net(browser)
        any_site_page_object.mouse_over_video_info_net(browser)
        implement_download_file(browser, get_current_download_folder, file_size=1.00),


class TestBongda24h:

    @pytestrail.case('C98788')
    def test_download_file_bong_da_24h(self, browser, get_current_download_folder
                                       , clear_download_page):
        browser.get(OtherSiteUrls.BONG_DA_24H_VIDEO_URL)
        any_site_page_object.click_video_bong_da_24h(browser)
        any_site_page_object.mouse_over_video_bong_da_24h(browser)
        implement_download_file(browser, get_current_download_folder),


class TestKeoNhaCai:

    @pytestrail.case('C98792')
    @pytestrail.defect('BR-1200')
    @pytest.mark.skip('Cannot convert to mp4 due to BR-1200')
    def test_download_file_keo_nha_cai(self, browser, get_current_download_folder
                                       , clear_download_page, revert_high_quality_default_option):
        choose_video_quality_medium_option(browser)
        browser.get(OtherSiteUrls.KEO_NHA_CAI_VIDEO_URL)
        any_site_page_object.click_video_item_keo_nha_cai(browser)
        any_site_page_object.mouse_over_video_item_keo_nha_cai(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestVoV:

    @pytestrail.case('C98798')
    def test_download_file_vov(self, browser, get_current_download_folder
                               , clear_download_page
                               , enable_ublock_plus_extension):
        browser.get(OtherSiteUrls.VOV_VIDEO_URL)
        any_site_page_object.switch_to_frame_vov_vn(browser)
        any_site_page_object.play_vov_vn_video(browser)
        browser.switch_to.default_content()
        any_site_page_object.mouse_over_video_item_vov_vn(browser)
        implement_download_file(browser, get_current_download_folder, time_sleep=8, ),


class TestDoiSongPhapLuat:

    @pytestrail.case('C98776')
    def test_download_doi_song_phap_luat(self, browser, get_current_download_folder
                                         , clear_download_page):
        browser.get(OtherSiteUrls.DOI_SONG_PHAP_LUAT_VIDEO_URL)
        any_site_page_object.click_video_item_doi_song_phap_luat(browser)
        any_site_page_object.mouse_over_video_doi_song_phap_luat(browser)
        implement_download_file(browser, get_current_download_folder),


class TestSaoStar:

    @pytestrail.case('C98785')
    @pytestrail.defect('PF-497')
    def test_download_sao_star(self, browser, get_current_download_folder
                               , clear_download_page):
        browser.get(OtherSiteUrls.SAO_STAR_VIDEO_URL)
        any_site_page_object.mouse_over_video_sao_star_vn(browser)
        implement_download_file(browser, get_current_download_folder),


class TestBestieVN:

    @pytestrail.case('C98791')
    def test_download_bestie_vn_video(self, browser, get_current_download_folder
                                      , clear_download_page
                                      , choose_low_quality_option, revert_high_quality_default_option):
        browser.get(OtherSiteUrls.BESTIE_VN_VIDEO_URL)
        any_site_page_object.switch_to_first_iframe_bestie_vn(browser)
        any_site_page_object.switch_to_second_iframe_bestie_vn(browser)
        any_site_page_object.mouse_over_video_bestie_vn(browser)
        implement_download_file(browser, get_current_download_folder),


class TestVtvGoVN:

    @pytestrail.case('C98796')
    def test_download_vtv_go_vn(self, browser, get_current_download_folder
                                , clear_download_page):
        browser.get(OtherSiteUrls.VTV_GO_VN_VIDEO_URL)
        any_site_page_object.mouse_over_video_vtv_go_vn(browser)
        implement_download_file(browser, get_current_download_folder)
