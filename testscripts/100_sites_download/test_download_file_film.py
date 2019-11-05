import pytest
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.common_setup import implement_download_file, \
    clear_data_download_in_browser_and_download_folder, pause_any_video_site, \
    handle_windows_watch_option, check_if_the_file_fully_downloaded, assert_file_download_exist
from utils_automation.const import OtherSiteUrls
from utils_automation.setup import WaitAfterEach

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()


class TestPhimmoi:

    @staticmethod
    def prepare_displayed_savior_popup(browser):
        browser.get(OtherSiteUrls.PHIMMOI_VIDEO_URL)
        windows_list = browser.window_handles
        print(windows_list)
        if len(windows_list) >= 2:
            browser.switch_to.window(windows_list[0])
            any_site_page_object.close_popup_continue_watching(browser)
            browser.switch_to_active_element()
            if any_site_page_object.verify_exist_ads_pop_up_phim_moi(browser) > 0:
                any_site_page_object.close_image_popup_phim_moi(browser)
            browser.switch_to_default_content()
        else:
            any_site_page_object.close_popup_continue_watching(browser)
        browser.switch_to_default_content()
        any_site_page_object.mouse_over_video_element_phimmoi(browser)

    @pytestrail.case('C96721')
    @pytest.mark.ten_popular_sites
    def test_download_file_phim_moi(self, browser, get_current_download_folder
                                    , clear_download_page_and_download_folder):
        self.prepare_displayed_savior_popup(browser)
        implement_download_file(browser, get_current_download_folder, )


class TestVuViPhim:

    @staticmethod
    def prepare_savior_option_displayed(browser):
        browser.get(OtherSiteUrls.VU_VI_PHIM_VIDEO_URL)
        # any_site_page_object.click_video_item_vu_vi_phim_js(browser)
        any_site_page_object.switch_to_iframe_vu_vi_phim(browser)
        # any_site_page_object.click_video_item_vu_vi_phim(browser)
        any_site_page_object.click_replay_btn_vu_vi_phim(browser)
        any_site_page_object.mouse_over_video_item_vu_vi_phim(browser)
        WaitAfterEach.sleep_timer_after_each_step()

    @pytestrail.case('C98751')
    @pytest.mark.skip(reason='Not stable for mouse over to click on download')
    def test_download_file_vuviphim(self, browser, get_current_download_folder
                                    , clear_download_page_and_download_folder):
        self.prepare_savior_option_displayed(browser)
        browser.switch_to.default_content()
        implement_download_file(browser, get_current_download_folder, ),
        clear_data_download_in_browser_and_download_folder(browser, get_current_download_folder)


class TestTvZing:

    @pytestrail.case('C96763')
    @pytest.mark.ten_popular_sites
    def test_download_file_tv_zing(self, browser, get_current_download_folder
                                   , clear_download_page_and_download_folder):
        pause_any_video_site(browser, OtherSiteUrls.TV_ZING_VIDEO_URL)
        implement_download_file(browser, get_current_download_folder, )


class TestTVHay:

    @pytestrail.case('C98762')
    def test_download_file_video_tv_hay(self, browser, get_current_download_folder
                                        , clear_download_page_and_download_folder):
        browser.get(OtherSiteUrls.TV_HAY_VIDEO_URL)
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        any_site_page_object.switch_to_tv_hay_iframe_level_1(browser)
        any_site_page_object.switch_to_tv_hay_iframe_level_2(browser)
        any_site_page_object.click_play_btn_tv_hay(browser)
        while "0:00" in any_site_page_object.get_video_time_tv_hay(browser):
            WaitAfterEach.sleep_timer_after_each_step()
        browser.switch_to.default_content()
        any_site_page_object.mouse_over_video_item_tv_hay(browser)
        savior_page_object.download_file_via_savior_download_btn(browser)
        savior_page_object.download_file_title_via_savior_download_btn(browser, 'Xem Phim')
        WaitAfterEach.sleep_timer_after_each_step()
        check_if_the_file_fully_downloaded(browser)
        assert_file_download_exist(get_current_download_folder)


class TestAnimeSub:

    @pytestrail.case('C98781')
    @pytestrail.defect('PF-559')
    @pytest.mark.skip(reason='Cannot detect video')
    def test_download_file_video_anime_sub(self, browser, get_current_download_folder
                                           , clear_download_page_and_download_folder):
        browser.get(OtherSiteUrls.ANIME_VSUB_TV_URL)
        handle_windows_watch_option(browser, any_site_page_object.choose_continue_from_start_anime_subtv(browser))
        any_site_page_object.close_and_watch_ad_button_anime_subtv(browser)
        any_site_page_object.mouse_over_video_anime_vsub_tv(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestAnimeTVN:

    @pytestrail.case('C98803')
    @pytestrail.defect('US-43')
    @pytest.mark.skip(reason='Cannot video file on link')
    def test_download_file_video_anime_tvn(self, browser, get_current_download_folder
                                           , clear_download_page_and_download_folder):
        browser.get(OtherSiteUrls.ANIME_TVN_VIDEO_URL)
        any_site_page_object.mouse_over_tvn_video_element(browser)
        implement_download_file(browser, get_current_download_folder)


class TestPhimBatHu:

    @pytestrail.case('C98804')
    @pytest.mark.usefixtures('clear_download_page_and_download_folder')
    def test_download_file_video_phim_bat_hu(self, browser, get_current_download_folder
                                             , clear_download_page_and_download_folder):
        browser.get(OtherSiteUrls.PHIM_BAT_HU_VIDEO_URL)
        # any_site_page_object.click_video_phim_bat_hu_video_element(browser)
        any_site_page_object.mouse_over_phim_bat_hu_video_element(browser)
        implement_download_file(browser, get_current_download_folder),


class TestAnimeHayTV:

    @pytestrail.case('C98723')
    def test_download_file_video_anime_hay_tv(self, browser, get_current_download_folder
                                              , clear_download_page_and_download_folder):
        browser.get(OtherSiteUrls.ANIME_HAY_TV_VIDEO_URL)
        any_site_page_object.mouse_over_video_wrapper_element_anime_hay_tv(browser)
        any_site_page_object.switch_to_iframe_anime_hay_tv(browser)
        implement_download_file(browser, get_current_download_folder, ),


class TestVietSubTV:

    @pytestrail.case('C98786')
    def test_download_file_video_vietsub_tv(self, browser, get_current_download_folder
                                            , clear_download_page_and_download_folder):
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







