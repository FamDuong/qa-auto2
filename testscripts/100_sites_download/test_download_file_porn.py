import pytest
from pytest_testrail.plugin import pytestrail
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from testscripts.common_setup import implement_download_file, download_file_via_main_download_button, \
    get_resolution_info, assert_file_download_value, delete_all_mp4_file_download
from utils_automation.const import OtherSiteUrls
from utils_automation.setup import WaitAfterEach

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()
top_sites_savior_title_action = TopSitesSaviorTitleAction()


class TestXVideos:

    @pytestrail.case('C96723')
    @pytestrail.defect('PF-859')
    @pytest.mark.ten_popular_sites
    @pytest.mark.skip(reason='Cannot detect video PF-859')
    def test_download_file_x_videos(self, browser, get_current_download_folder, clear_download_page):
        browser.get(OtherSiteUrls.XVIDEOS_DOT_COM_VIDEO_URL)
        title = top_sites_savior_title_action.get_x_videos_title_video(browser)
        try:
            any_site_page_object.click_video_x_videos(browser)
            any_site_page_object.mouse_over_video_x_videos(browser)
            implement_download_file(browser, get_current_download_folder, startwith=title)
        finally:
            delete_all_mp4_file_download(get_current_download_folder, '.mp4', startwith=title)


class TestXNXX:

    @pytestrail.case('C96754')
    @pytestrail.defect('PF-833')
    @pytest.mark.ten_popular_sites
    @pytest.mark.skip(reason='Skip due to bug PF-833')
    def test_download_file_xnxx_videos(self, browser, get_current_download_folder
                                    , clear_download_page):
        browser.get(OtherSiteUrls.XNXX_VIDEO_URL)
        title = top_sites_savior_title_action.get_xnxx_video_title(browser)
        try:
            any_site_page_object.click_play_video_item_xnxx(browser)
            any_site_page_object.mouse_over_video_xnxx(browser)
            implement_download_file(browser, get_current_download_folder, startwith=title),
        finally:
            delete_all_mp4_file_download(get_current_download_folder, '.mp4', startwith=title)


class TestPornHub:

    @pytestrail.case('C98771')
    @pytestrail.defect('PF-620')
    @pytest.mark.ten_popular_sites
    def test_download_file_porn_hub(self, browser, get_current_download_folder
                                    , clear_download_page, ):
        browser.get(OtherSiteUrls.FR_PORN_HUB_VIDEO_URL)
        any_site_page_object.click_video_fr_porn_hub(browser)
        any_site_page_object.mouse_over_video_fr_porn_hub(browser)
        implement_download_file(browser, get_current_download_folder, )


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













