import time

import pytest
from selenium.common.exceptions import NoAlertPresentException

from models.pageelements.sites import AnySiteElements
from models.pageelements.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleElements
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail

from models.pageobject.top_savior_sites.top_savior_sites_film import TopSaviorSitesFilmActions
from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from testscripts.common_setup import implement_download_file, \
    clear_data_download_in_browser_and_download_folder, \
    handle_windows_watch_option, check_if_the_file_fully_downloaded, assert_file_download_exist, \
    delete_all_mp4_file_download
from utils_automation.common import WebElements
from utils_automation.const import OtherSiteUrls
from utils_automation.setup import WaitAfterEach

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()
top_sites_savior_title_action = TopSitesSaviorTitleAction()


class TestPhimmoi:

    top_sites_savior_actions = TopSaviorSitesFilmActions()
    top_sites_savior_title_actions = TopSitesSaviorTitleAction()
    top_sites_savior_title_elements = TopSitesSaviorTitleElements()

    def test_prepare_displayed_savior_popup(self, browser):
        browser.get(OtherSiteUrls.PHIMMOI_VIDEO_URL)
        browser.refresh()
        # self.top_sites_savior_actions.open_film_in_phim_moi(browser)
        self.top_sites_savior_actions.close_popup_ad_if_appear(browser)
        # time.sleep(40)
        WebElements.scroll_into_view_element(browser, self.top_sites_savior_title_elements
                                             .find_video_phimmoi_title_element(browser))
        any_site_page_object.mouse_over_video_element_phimmoi(browser)
        time.sleep(400)

    @pytestrail.case('C96721')
    @pytest.mark.ten_popular_sites
    @pytestrail.defect('PF-1219')
    def test_download_file_phim_moi(self, browser, get_current_download_folder):
                                    #, clear_download_page ,):
        self.prepare_displayed_savior_popup(browser)
        video_title_start_with = self.top_sites_savior_title_actions.get_phimmoi_video_title(browser)
        try:
            implement_download_file(browser, get_current_download_folder, startwith=video_title_start_with)
        finally:
            delete_all_mp4_file_download(get_current_download_folder, '.mp4', startwith=video_title_start_with)


class TestVuViPhim:

    any_site_element = AnySiteElements()

    def prepare_savior_option_displayed(self, browser):
        browser.get(OtherSiteUrls.VU_VI_PHIM_VIDEO_URL)
        any_site_page_object.switch_to_iframe_vu_vi_phim(browser)
        any_site_page_object.play_video_by_javascript(browser)
        # any_site_page_object.play_video_vu_vi_phim(browser)
        browser.switch_to.default_content()
        any_site_page_object.mouse_over_video_vu_vi_phim(browser)

    @pytestrail.case('C98751')
    def test_download_file_vuviphim(self, browser, get_current_download_folder):
        self.prepare_savior_option_displayed(browser)
        implement_download_file(browser, get_current_download_folder, ),
        clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)


class TestTvZing:

    top_savior_sites_film_actions = TopSaviorSitesFilmActions()
    top_sites_savior_title_actions = TopSitesSaviorTitleAction()

    @pytestrail.case('C96763')
    @pytest.mark.ten_popular_sites
    def test_download_file_tv_zing(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.TV_ZING_VIDEO_URL)
        self.top_savior_sites_film_actions.close_login_popup_tv_zing(browser)
        browser.switch_to.default_content()
        video_title = self.top_sites_savior_title_actions.get_tv_zing_video_title(browser)
        try:
            any_site_page_object.click_first_video_element(browser)
            any_site_page_object.mouse_over_first_video_element(browser)
            implement_download_file(browser, get_current_download_folder, startwith=video_title)
        finally:
            delete_all_mp4_file_download(get_current_download_folder, '.mp4', startwith=video_title)


class TestTVHay:

    @pytestrail.case('C98762')
    def test_download_file_video_tv_hay(self, browser, get_current_download_folder
                                        , clear_download_page):
        browser.get(OtherSiteUrls.TV_HAY_VIDEO_URL)
        video_title = self.top_sites_savior_title_actions.get_tv_zing_video_title(browser)
        try:
            any_site_page_object.switch_to_tv_hay_iframe(browser)
            any_site_page_object.click_play_btn_tv_hay(browser)
            any_site_page_object.skip_ads_tv_hay(browser)
            any_site_page_object.click_video_item_tv_hay(browser)
            # while "0:00" in any_site_page_object.get_video_time_tv_hay(browser):
            #     WaitAfterEach.sleep_timer_after_each_step()
            browser.switch_to.default_content()
            any_site_page_object.mouse_over_video_item_tv_hay(browser)
            savior_page_object.download_file_via_savior_download_btn(browser)
            savior_page_object.download_file_title_via_savior_download_btn(browser, 'Xem Phim')
            # WaitAfterEach.sleep_timer_after_each_step()
            # check_if_the_file_fully_downloaded(browser)
            # assert_file_download_exist(get_current_download_folder)
            implement_download_file(browser, get_current_download_folder, startwith=video_title)
        finally:
            delete_all_mp4_file_download(get_current_download_folder, '.mp4', startwith=video_title)


class TestAnimeSub:

    @pytestrail.case('C98781')
    @pytestrail.defect('PF-559')
    def test_download_file_video_anime_sub(self, browser, get_current_download_folder
                                           , clear_download_page):
        browser.get(OtherSiteUrls.ANIME_VSUB_TV_URL)
        try:
            browser.switch_to.alert.dismiss()
        except NoAlertPresentException as e:
            print(e.stacktrace)
        any_site_page_object.wait_until_player_finish_loading_anime_vsub_tv(browser)
        handle_windows_watch_option(browser, any_site_page_object.choose_continue_from_start_anime_subtv)
        any_site_page_object.click_play_button_anime_vsub_tv(browser)
        any_site_page_object.mouse_over_video_anime_vsub_tv(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestAnimeTVN:

    @pytestrail.case('C98803')
    @pytestrail.defect('US-43')
    @pytest.mark.skip(reason='Cannot video file on link')
    def test_download_file_video_anime_tvn(self, browser, get_current_download_folder
                                           , clear_download_page):
        browser.get(OtherSiteUrls.ANIME_TVN_VIDEO_URL)
        any_site_page_object.mouse_over_tvn_video_element(browser)
        implement_download_file(browser, get_current_download_folder)


class TestPhimBatHu:

    @pytestrail.case('C98804')
    @pytest.mark.usefixtures('clear_download_page_and_download_folder')
    def test_download_file_video_phim_bat_hu(self, browser, get_current_download_folder
                                             , clear_download_page):
        browser.get(OtherSiteUrls.PHIM_BAT_HU_VIDEO_URL)
        # any_site_page_object.click_video_phim_bat_hu_video_element(browser)
        any_site_page_object.mouse_over_phim_bat_hu_video_element(browser)
        implement_download_file(browser, get_current_download_folder),


class TestAnimeHayTV:

    @pytestrail.case('C98723')
    def test_download_file_video_anime_hay_tv(self, browser, get_current_download_folder
                                              , clear_download_page):
        browser.get(OtherSiteUrls.ANIME_HAY_TV_VIDEO_URL)
        any_site_page_object.mouse_over_video_wrapper_element_anime_hay_tv(browser)
        any_site_page_object.switch_to_iframe_anime_hay_tv(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestVietSubTV:

    @pytestrail.case('C98786')
    def test_download_file_video_vietsub_tv(self, browser, get_current_download_folder
                                            , clear_download_page
                                            , enable_ublock_plus_extension):
        browser.get(OtherSiteUrls.VIET_SUB_TV_VIDEO_URL)
        any_site_page_object.play_video_viet_sub_tv(browser)
        any_site_page_object.mouse_over_video_item_viet_sub_tv(browser)
        savior_page_object.download_file_via_savior_download_btn(browser)
        WaitAfterEach.sleep_timer_after_each_step()
        savior_page_object.download_file_title_via_savior_download_btn(browser, 'VietSub')
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        # Check the file is fully downloaded
        check_if_the_file_fully_downloaded(browser, )
        assert_file_download_exist(get_current_download_folder)


class TestVtv16Info:

    @pytestrail.case('C98732')
    def test_download_file_video_vtv16_info(self, browser, get_current_download_folder
                                            , clear_download_page):
        browser.get(OtherSiteUrls.VTV16_INFO_VIDEO_URL)
        any_site_page_object.mouse_over_video_vtv16_info_net(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestClipAnime:

    @pytestrail.case('C98742')
    def test_download_file_video_clip_anime(self, browser, get_current_download_folder
                                            , clear_download_page):
        browser.get(OtherSiteUrls.CLIP_ANIME_VN_VIDEO_URL)
        any_site_page_object.mouse_over_clip_anime_com(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestMotPhimNet:

    @pytestrail.case('C98756')
    @pytestrail.defect('PF-541')
    # @pytest.mark.skip(reason='Cannot download file video motphim')
    def test_download_file_film_mot_phim_net(self, browser, get_current_download_folder
                                             , clear_download_page):
        browser.get(OtherSiteUrls.MOT_PHIM_VIDEO_URL)
        time.sleep(2)
        any_site_page_object.click_video_item_mot_phim(browser)
        time.sleep(5)
        any_site_page_object.mouse_over_video_item_mot_phim(browser, url=OtherSiteUrls.MOT_PHIM_VIDEO_URL)
        implement_download_file(browser, get_current_download_folder, )


class TestXemVtvNet:

    @pytestrail.case('C98800')
    @pytestrail.defect('PF-512')
    def test_download_video_xem_vtv_net(self, browser, get_current_download_folder
                                        , clear_download_page):
        browser.get(OtherSiteUrls.XEM_VTV_NET)
        any_site_page_object.click_play_btn_xem_vtv_net(browser)
        any_site_page_object.mouse_over_video_xem_vtv_net(browser)
        implement_download_file(browser, get_current_download_folder,)