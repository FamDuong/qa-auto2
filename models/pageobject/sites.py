import time
import logging
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from models.pageelements.sites import YoutubePageElements, GooglePageElements, AnySiteElements
from models.pagelocators.sites import AnySite
from models.pageobject.basepage_object import BasePageObject
from utils_automation.common import WebElements
from utils_automation.setup import WaitAfterEach

LOGGER = logging.getLogger(__name__)


class YoutubePageObject(BasePageObject):
    youtube_element = YoutubePageElements()

    def choose_any_video_item(self, driver, text):
        profile_path_elem = self.youtube_element.find_any_video_item(driver, text)
        WaitAfterEach.sleep_timer_after_each_step()
        return profile_path_elem.get_attribute('href')

    def search_video_item(self, driver, text):
        self.youtube_element.search_video(driver, text)
        WaitAfterEach.sleep_timer_after_each_step()

    def mouse_over_video_item(self, driver):
        self.mouse_over_video_element_site(driver, self.youtube_element.find_video_player_item(driver))

    def click_video_item(self, driver):
        self.youtube_element.find_video_player_item(driver).click()
        WaitAfterEach.sleep_timer_after_each_step()


class GooglePageObject(BasePageObject):
    google_element = GooglePageElements()

    def search_with_value(self, driver, text_value):
        search_field = self.google_element.find_search_field(driver)
        search_field.click()
        search_field.send_keys(text_value)
        search_field.send_keys(Keys.RETURN)
        WaitAfterEach.sleep_timer_after_each_step()

    def search_result_video(self, driver):
        self.google_element.find_video_search_btn(driver).click()

    def download_via_savior_icon_button(self, driver):
        self.google_element.find_savior_icon(driver).click()


class AnySitePageObject(BasePageObject):
    any_site_element = AnySiteElements()

    def mouse_over_video_iframe(self, driver, switch_to_iframe_video, find_video_item, time_out_sec, *args):
        start_time = datetime.now()
        driver.switch_to.default_content()
        while self.verify_savior_popup_appear(driver) is None:
            switch_to_iframe_video(driver)
            WebElements.mouse_over_element(driver, find_video_item(driver))
            for arg in args:
                arg
                time.sleep(1)
            driver.switch_to.default_content()
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= time_out_sec:
                break

    def mouse_over_video_iframe_with_minimize_maximize(self, driver, switch_to_iframe_video, find_video_item,
                                                       time_out_sec):
        self.mouse_over_video_iframe(driver, switch_to_iframe_video, find_video_item, time_out_sec,
                                     driver.minimize_window(),
                                     driver.maximize_window())

    def mouse_over_first_video_element(self, driver, element=AnySite.FIRST_VIDEO):
        first_video_element = self.any_site_element.find_first_video_element(driver, element)
        self.mouse_over_video_element_site(driver, first_video_element)
        start_time = datetime.now()
        while first_video_element is None:
            first_video_element = self.any_site_element.find_first_video_element(driver, element)
            self.mouse_over_video_element_site(driver, first_video_element)
            time.sleep(2)
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 10:
                break

    def mouse_over_nhaccuatui_music_element(self, driver):
        music_element = self.any_site_element.find_nhaccuatui_music_element(driver)
        self.mouse_over_video_element_site(driver, music_element)

    def mouse_over_soundcloud_music_element(self, driver):
        music_element = self.any_site_element.find_soundcloud_music_element(driver)
        self.mouse_over_video_element_site(driver, music_element)

    def get_mouse_enter_event_js_element(self, driver):
        return driver.execute_script('return new Event("mouseenter")')

    def find_video_element_vu_vi_phim_js(self, driver):
        return driver.execute_script('return document.querySelector("#media > iframe")')

    def send_event_mouse_over_vu_vi_phim_js(self, driver):
        driver.execute_script('document.querySelector("#media > iframe").dispatchEvent(new Event("mouseenter"))')

    def click_first_video_element(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        self.any_site_element.click_first_video_element(driver)

    def click_video_element_24h(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        self.any_site_element.find_video_element_24h(driver).click()

    def mouse_over_video_element_24h(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_element_24h(driver))

    def mouse_over_video_element_phimmoi(self, driver):
        driver.execute_script('element = document.querySelector("#media-player > div.jw-media.jw-reset > video");'
                              'element.dispatchEvent(new Event("mouseenter"));')

    def mouse_leave_video_element_phimmoi(self, driver):
        driver.execute_script('element = document.querySelector("#media-player > div.jw-media.jw-reset > video");'
                              'element.dispatchEvent(new Event("mouseleave"));')

    def mouse_over_video_element_player_embed_phimmoi(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_embed_player_phimmoi(driver)
                                           , timeout_verify_savior_popup=10)

    def mouse_over_video_iframe_phimmoi(self, driver):
        self.mouse_over_video_element_site(driver,
                                           self.any_site_element.find_video_element_mouse_over_iframe_phimmoi(driver))

    def switch_to_video_iframe_phimmoi(self, driver: WebDriver):
        driver.switch_to.frame(self.any_site_element.find_video_element_mouse_over_iframe_phimmoi(driver))

    def verify_exist_ads_pop_up_phim_moi(self, driver):
        return len(self.any_site_element.find_elements_close_pop_up_ads_phim_moi(driver))

    def mouse_over_video_element_facebook(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_in_facebook_page(driver))

    def mouse_over_video_element_messenger_chat(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_in_messenger_chat(driver))

    def click_video_element_messenger_chat(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        try:
            self.any_site_element.find_play_button_in_messenger_chat(driver).click()
        except:
            pass

    def mouse_over_video_element_instagram(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_in_instagram(driver))

    def mouse_over_video_item_kienthuc(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_in_kienthuc(driver))

    def click_video_item_kienthuc(self, driver):
        ActionChains(driver).move_to_element(self.any_site_element.find_video_item_in_kienthuc(driver)).perform()
        self.any_site_element.find_video_item_in_kienthuc(driver).click()

    def mouse_over_video_item_eva_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_eva_vn(driver))

    def choose_media_view_option_twitter(self, driver):
        self.any_site_element.find_media_view_option_twitter(driver).click()

    def handle_user_restricted_twitter(self, driver):
        elements = self.any_site_element.find_elements_user_restricted_twitter(driver)
        print('Elements restricted_user_twitter got are :', elements)
        if len(elements) > 0:
            driver.execute_script('document.querySelector(arguments[0]).click()',
                                  AnySite.TWITTER_AUTHORIZE_RESTRICTED_USER_BTN_JAVASCRIPT)
        else:
            print('This twitter user is not restricted')

    def mouse_over_video_item_twitter(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_twitter(driver))

    def mouse_over_video_item_soha(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_soha(driver))

    def mouse_over_video_item_sao_2_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_2sao_vn(driver), timeout=30)

    def click_video_item_sao_2_vn(self, driver):
        self.any_site_element.find_video_item_2sao_vn(driver).click()

    def mouse_over_video_item_phunu_giadinh(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_phunu_giadinh(driver))

    def click_video_item_phunu_giadinh(self, driver):
        self.any_site_element.find_video_item_phunu_giadinh(driver).click()

    def mouse_over_video_item_tien_phong(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_tien_phong(driver))

    def click_video_item_tien_phong(self, driver):
        ActionChains(driver).move_to_element(self.any_site_element.find_play_video_item_tien_phong(driver)).perform()
        self.any_site_element.find_play_video_item_tien_phong(driver).click()

    def mouse_over_video_item_bong_da_dot_com(self, driver):
        self.mouse_over_video_element_site(driver,
                                           self.any_site_element.find_video_item_bong_da_dot_com(driver),
                                           20)

    def click_video_item_bong_da_dot_com(self, driver):
        ActionChains(driver).move_to_element(self.any_site_element.find_video_item_bong_da_dot_com(driver)).perform()
        self.any_site_element.find_video_item_bong_da_dot_com(driver).click()

    def mouse_over_video_item_gia_dinh_dot_net(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_gia_dinh_dot_net(driver))

    def mouse_over_video_item_a_family(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_a_family(driver))

    def mouse_over_video_item_gamek_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_gamek_vn(driver))

    def click_video_item_an_ninh_thu_do(self, driver):
        self.any_site_element.find_video_item_an_ninh_thu_do(driver).click()

    def mouse_over_video_item_an_ninh_thu_do(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_an_ninh_thu_do(driver))

    def mouse_over_video_item_tuoi_tre(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_tuoi_tre(driver))

    def click_video_item_mot_phim(self, driver):
        ActionChains(driver).move_to_element(
            self.any_site_element.find_play_button_video_mot_phim(driver)).click().perform()

    def mouse_over_video_mot_phim(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_tuoi_tre(driver))

    def click_video_episode_mot_phim(self, driver):
        self.any_site_element.find_video_episode_mot_phim(driver).click()

    def click_video_box_player_mot_phim(self, driver):
        self.any_site_element.find_video_box_player_mot_phim(driver).click()

    def switch_to_video_iframe_mot_phimzz(self, driver):
        driver.switch_to.frame(self.any_site_element.find_video_iframe_mot_phimzz(driver))

    def click_to_play_button_mot_phimzz(self, driver):
        self.any_site_element.find_play_button_mot_phimzz(driver).click()

    def mouse_over_then_click_play_video_mot_phimzz(self, driver):
        # self.switch_to_video_iframe_mot_phimzz(driver)
        # self.click_to_play_button_mot_phimzz(driver)
        self.mouse_over_video_iframe(driver, self.switch_to_video_iframe_mot_phimzz,
                                     self.any_site_element.find_video_item_mot_phimzz, 40)


    # def mouse_over_video_item_mot_phim(self, driver):
    #     # iframe = driver.find_element_by_css_selector("iframe[src*='//motphimzz']")
    #     # driver.switch_to.frame(iframe)
    #     driver.execute_script(f'document.querySelector("#player > iframe").src="iframe[src*=\'//motphimzz\']"')
    #     # time.sleep(8)
    #     driver.execute_script('document.querySelector("#player > iframe").dispatchEvent(new Event("mouseenter"));')
    #     time.sleep(3)

    def skip_ads_tv_hay(self, driver):
        self.any_site_element.find_skip_ads_btn_tv_hay(driver).click()

    def click_play_btn_tv_hay(self, driver):
        self.click_on_element_if_exist(self.any_site_element.find_play_btn_tv_hay(driver))

    def click_play_btn_in_frame_tv_hay(self, driver):
        self.click_on_element_if_exist(self.any_site_element.find_play_btn_in_frame_tv_hay(driver))

    def switch_to_tv_hay_iframe(self, driver):
        driver.switch_to.frame(self.any_site_element.find_iframe_tv_hay(driver))

    def mouse_over_video_item_tv_hay(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_tv_hay(driver))

    def get_video_time_tv_hay(self, driver):
        i = 0
        while i == 0:
            if driver.execute_script('return document.querySelector(arguments[0])',
                                     'div[class="html5-vpl_time_t"]') is not None:
                time_value = driver.execute_script('return document.querySelector(arguments[0]).textContent',
                                                   'div[class="html5-vpl_time_t"]')
                i += 1
                return time_value

    def click_pause_btn_tv_hay(self, driver):
        self.any_site_element.find_pause_btn_tv_hay(driver).click()

    def click_video_item_tv_hay(self, driver):
        driver.execute_script('document.querySelector("#embedVideoC > div.vid_play").click();')

    def mouse_over_video_item_ngoi_sao_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_ngoi_sao_vn(driver))

    def click_video_element_vtc_v(self, driver):
        self.any_site_element.find_video_play_item_vtc_vn(driver).click()

    def mouse_over_video_element_vtc_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_vtc_vn(driver))

    def mouse_over_video_element_kenh14_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_kenh14_vn(driver))

    def mouse_over_video_element_cafe_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_cafe_vn(driver))

    def mouse_over_video_element_tin_tuc_online_vn(self, driver):
        self.mouse_over_video_iframe(driver, self.switch_to_video_iframe_tin_tuc_online_vn,
                                     self.any_site_element.find_video_iframe_tin_tuc_online_vn,
                                     40)

    def mouse_over_video_detail_tin_tuc_online_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_detail_tin_tuc_online_vn(driver))

    def switch_to_video_iframe_tin_tuc_online_vn(self, driver):
        driver.switch_to.frame(self.any_site_element.find_video_iframe_tin_tuc_online_vn(driver))

    def click_video_giao_duc_thoi_dai(self, driver):
        self.any_site_element.find_video_item_giao_duc_thoi_dai(driver).click()

    def mouse_over_video_giao_duc_thoi_dai(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_giao_duc_thoi_dai(driver))

    def scroll_to_news_video_vnexpress_video(self, driver):
        driver.execute_script("document.querySelector('"+AnySite.NEWS_VNEXPRESS_VIDEO_CSS+"').scrollIntoView()")
        # self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_vn_express(driver))

    def mouse_over_video_thanh_nien_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_thanh_nien(driver))

    def click_video_thanh_nien_vn(self, driver):
        self.any_site_element.find_video_item_thanh_nien(driver).click()

    def mouse_over_video_dan_tri_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_dan_tri_vn(driver))

    def click_play_video_dan_tri_vn(self, driver):
        self.any_site_element.find_play_btn_dan_tri_vn(driver).click()

    def mouse_over_video_nguoi_lao_dong_tv(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_nguoi_lao_dong_tv(driver),
                                           timeout=30)

    def click_video_nguoi_lao_dong_tv(self, driver):
        self.any_site_element.find_nguoi_lao_dong_pause_btn(driver).click()

    def click_video_anime_vsub_tv(self, driver):
        self.any_site_element.find_video_item_anime_sub_tv(driver).click()

    def mouse_over_video_anime_vsub_tv(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_anime_sub_tv(driver))

    def click_play_button_anime_vsub_tv(self, driver):
        self.any_site_element.find_play_btn_anime_vsub_tv(driver).click()

    def choose_continue_from_start_anime_subtv(self, driver):
        self.any_site_element.find_continue_from_start_popup_btn_anime_sub_tv(driver).click()

    def wait_until_player_finish_loading_anime_vsub_tv(self, driver):
        self.any_site_element.find_wait_for_player_load_anime_vsub_tv(driver)
        start_time = datetime.now()
        while len(self.any_site_element.find_elements_wait_for_player_load_anime_vsub_tv(driver)) >= 1:
            time.sleep(2)
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 30:
                break

    def close_and_watch_ad_button_anime_subtv(self, driver):
        self.any_site_element.find_close_ad_btn_anime_vsub_tv(driver).click()

    def mouse_over_video_nhac_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_nhac_vn(driver))

    def click_video_x_videos(self, driver):
        self.any_site_element.find_play_btn_x_videos(driver).click()

    def mouse_over_video_x_videos(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_xvideos(driver), timeout=20)

    def mouse_over_video_xnxx(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_xnxx(driver))

    def click_play_video_item_xnxx(self, driver):
        ActionChains(driver).move_to_element(self.any_site_element.find_play_btn_xnxx(driver)).perform()
        self.any_site_element.find_play_btn_xnxx(driver).click()

    def click_video_fr_porn_hub(self, driver):
        try:
            elem = self.any_site_element.find_video_play_btn_fr_porn_hub(driver)
            if elem is not None:
                try:
                    elem.click()
                except:
                    pass
        except NoSuchElementException as e:
            print(e.stacktrace)

    def mouse_over_video_fr_porn_hub(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_fr_porn_hub(driver))

    def click_play_video_xhamster_one(self, driver):
        play_video_btn = self.any_site_element.find_play_button_video_item_xhamster_one(driver)
        play_video_btn.click()

    def click_video_vlxx(self, driver):
        ActionChains(driver).move_to_element(self.any_site_element.find_video_item_wrapper_vlxx(driver)).perform()
        self.any_site_element.find_video_item_wrapper_vlxx(driver).click()

    def mouse_over_video_vlxx(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_vlxx(driver))

    def click_video_sex_top1(self, driver):
        self.any_site_element.find_video_item_wrapper_sex_top1(driver).click()

    def mouse_over_video_sex_top1(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_sex_top1(driver))

    def click_video_sex_hihi(self, driver):
        self.any_site_element.find_video_item_wrapper_sex_hihi(driver).click()

    def mouse_over_video_sex_hihi(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_sex_hihi(driver))

    def click_video_jav_hd_pro(self, driver):
        self.any_site_element.find_video_wrapper_jav_hd_pro(driver).click()

    def mouse_over_video_jav_hd_pro(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_jav_hd_pro(driver))

    def click_video_phim_sex_porn(self, driver):
        self.any_site_element.find_phim_sex_porn_play_btn(driver).click()

    def mouse_over_video_phim_sex_porn(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        start_time = datetime.now()
        while self.verify_savior_popup_appear(driver) is None:
            WebElements.mouse_over_element(driver, self.any_site_element.find_phim_sex_porn_video_item(driver))
            self.any_site_element.find_phim_sex_porn_video_item(driver).click()
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 20:
                break

    def switch_to_iframe_phim_sex_porn(self, driver):
        driver.switch_to.frame(self.any_site_element.find_iframe_phim_sex_porn_item(driver))

    def click_video_jav_phim(self, driver):
        self.any_site_element.find_video_phim_jav_phim_wrapper(driver).click()

    def mouse_over_video_jav_phim(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_phim_jav_phim_item(driver))

    def mouse_over_video_tin_moi(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_tin_moi(driver))

    def click_video_info_net(self, driver):
        driver.switch_to.frame(self.any_site_element.find_video_iframe_info_net(driver))
        self.click_on_element_if_exist(self.any_site_element.find_video_play_btn_info_net(driver))

    def mouse_over_video_info_net(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_info_net(driver))
        driver.switch_to.default_content()

    def mouse_over_video_bong_da_24h(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_bong_da_24h(driver))

    def click_video_bong_da_24h(self, driver):
        self.any_site_element.find_video_item_bong_da_24h(driver).click()

    def click_video_item_keo_nha_cai(self, driver):
        self.any_site_element.find_video_item_keo_nha_cai(driver).click()

    def mouse_over_video_item_keo_nha_cai(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_keo_nha_cai(driver))

    def mouse_over_video_item_daily_motion(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_daily_motion(driver))

    def switch_to_frame_vov_vn(self, driver):
        driver.switch_to.frame(self.any_site_element.find_video_vov_vn_iframe(driver))

    def play_vov_vn_video(self, driver):
        self.any_site_element.find_vov_vn_play_btn(driver).click()

    def mouse_over_video_item_vov_vn(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        start_time = datetime.now()
        while self.verify_savior_popup_appear(driver) is None:
            WebElements.mouse_over_element(driver, self.any_site_element.find_video_vov_vn_iframe(driver))
            self.click_video_item_vov_vn(driver)
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 20:
                break

    def click_video_item_vov_vn(self, driver):
        self.any_site_element.find_video_vov_vn(driver).click()

    def mouse_over_video_element_sex_ngon(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_sex_ngon(driver))

    def click_video_element_sex_ngon(self, driver):
        self.any_site_element.find_video_sex_ngon(driver).click()

    def mouse_over_video_element_weibo(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_weibo(driver))

    def play_video_vu_vi_phim(self, driver):
        self.click_on_element_if_exist(self.any_site_element.find_play_btn_vu_vi_phim(driver))

    def switch_to_iframe_vu_vi_phim(self, driver):
        LOGGER.info("Switch to iframe")
        driver.switch_to.frame(self.any_site_element.find_frame_vu_vi_phim(driver))
        time.sleep(3)

    def mouse_over_video_vu_vi_phim(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_frame_vu_vi_phim(driver))

    def choose_server_anime_tvn(self, driver, server_number):
        self.any_site_element.find_server_anime_tvn(driver, server_number).click()

    def mouse_over_tvn_video_element(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_anime_tvn(driver))

    def mouse_over_phim_bat_hu_video_element(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        start_time = datetime.now()
        while self.verify_savior_popup_appear(driver) is None:
            # WebElements.mouse_over_element(driver, self.any_site_element.find_video_phim_bat_hu(driver))
            # WebElements.mouse_over_element(driver, self.any_site_element.find_video_phim_bat_hu_play(driver))
            driver.switch_to.frame(self.any_site_element.find_iframe_phim_bat_hu(driver))
            WebElements.mouse_over_element(driver, self.any_site_element.find_video_inner_phim_bat_hu(driver))
            self.any_site_element.find_video_inner_phim_bat_hu(driver).click()
            driver.switch_to.default_content()
            # self.any_site_element.find_video_phim_bat_hu(driver).click()
            # WaitAfterEach.sleep_timer_after_each_step()
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 30:
                break

    def click_video_phim_bat_hu_video_element(self, driver):
        self.any_site_element.find_video_phim_bat_hu_play(driver).click()

    def click_pause_video_phim_bat_hu(self, driver):
        self.any_site_element.find_pause_btn_phim_bat_hu(driver).click()

    def click_video_phim_sex_sub_video_element(self, driver):
        self.any_site_element.find_video_phim_sex_sub_wrapper(driver).click()

    def mouse_over_video_element_phim_sex_sub(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_phim_sex_sub_element(driver))

    def mouse_over_video_element_vlive_tv(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_vlive_tv_item(driver), timeout=50)

    def mouse_over_video_wrapper_element_anime_hay_tv(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_wrapper_anime_hay_tv(driver))

    def click_video_wrapper_element_anime_hay_tv(self, driver):
        self.any_site_element.find_video_wrapper_anime_hay_tv(driver).click()

    def switch_to_iframe_anime_hay_tv(self, driver):
        driver.switch_to.frame(self.any_site_element.find_video_iframe_anime_hay_tv(driver))

    def switch_to_iframe_doi_song_phap_luat(self, driver):
        driver.switch_to.frame(self.any_site_element.find_video_iframe_doi_song_phap_luat(driver))

    def click_video_item_doi_song_phap_luat(self, driver):
        self.switch_to_iframe_doi_song_phap_luat(driver)
        element = self.any_site_element.find_video_player_doi_song_phap_luat(driver)
        self.click_on_element_if_exist(element)
        while self.verify_savior_popup_appear(driver) is None:
            WaitAfterEach.sleep_timer_after_each_step()

    def mouse_over_video_doi_song_phap_luat(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_player_doi_song_phap_luat(driver))

    def mouse_over_video_sao_star_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_sao_star_video_item(driver))

    def play_video_viet_sub_tv(self, driver):
        while len(self.any_site_element.find_elements_play_middle_button_viet_sub_tv(driver)) >= 1:
            self.any_site_element.find_play_middle_button_viet_sub_tv(driver).click()
            WaitAfterEach.sleep_timer_after_each_step()
            if len(self.any_site_element.find_elements_ad_not_appear(driver)) >= 1:
                break

    def mouse_over_video_item_viet_sub_tv(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_viet_sub_tv_video_item(driver))

    def mouse_over_video_item_dong_phim(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_dong_phim_video_item(driver))

    def check_if_nhac_cua_tui_ads_appeared(self, driver):
        return len(self.any_site_element.find_nhac_cua_tui_ad_item(driver))

    def close_nhac_cua_tui_ad_item(self, driver):
        return self.any_site_element.find_nhac_cua_tui_ad_item_skip_button(driver=driver).click()

    def choose_watch_option_if_any(self, driver):
        elements = driver.find_elements_by_xpath(AnySite.DONG_PHIM_WATCH_OPTION_XPATH)
        start_time = datetime.now()
        if len(elements) == 0:
            while len(elements) == 0:
                time.sleep(2)
                elements = driver.find_elements_by_xpath(AnySite.DONG_PHIM_WATCH_OPTION_XPATH)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 15:
                    break
        elements = driver.find_elements_by_xpath(AnySite.DONG_PHIM_WATCH_OPTION_XPATH)
        if len(elements) > 0:
            self.any_site_element.wait_for_element(driver).until(
                ec.presence_of_element_located(AnySite.DONG_PHIM_WATCH_OPTION)).click()
        else:
            LOGGER.info("Cannot find button for watch options")
        return elements

    def click_video_item_dong_phim(self, driver):
        if len(self.any_site_element.find_elements_dong_phim_play_video_btn(driver)) >= 1:
            self.any_site_element.find_dong_phim_play_video_item(driver).click()

    def mouse_over_video_hentaiz_net(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_hentaiz_net_video_element(driver))

    def click_video_hentaiz_net(self, driver):
        self.any_site_element.find_hentaiz_net_play_btn(driver).click()

    def mouse_over_video_vtv16_info_net(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_vtv16_info_net_iframe(driver)
                                           , timeout=20)

    def mouse_over_video_bestie_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_bestie_vn_video_player(driver))

    def switch_to_first_iframe_bestie_vn(self, driver):
        driver.switch_to.frame(self.any_site_element.find_bestie_vn_iframe_1(driver))

    def switch_to_second_iframe_bestie_vn(self, driver):
        driver.switch_to.frame(self.any_site_element.find_bestie_vn_iframe_2(driver))

    def mouse_over_clip_anime_com(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_clip_anime_vn_video_player(driver))

    def mouse_over_video_vtv_go_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_vtv_go_vn_video_player(driver))

    def mouse_over_video_xem_vtv_net(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_xem_vtv_net_video_player(driver))

    def click_play_btn_xem_vtv_net(self, driver):
        element = self.any_site_element.find_xem_vtv_net_play_btn(driver)
        self.click_on_element_if_exist(element)

    def mouse_over_video_mot_phim(self, driver):
        import time
        time.sleep(10)
        iFrame1 = driver.find_element_by_xpath('//iframe[@src="//i.cherrystream.xyz/?slug=ctDSU3ZGG"]')
        driver.switch_to.frame(iFrame1)
        iFrame2 = driver.find_element_by_xpath('//iframe[@src="https://playhydrax.com/?v=ctDSU3ZGG"]')
        driver.switch_to.frame(iFrame2)
        import time
        time.sleep(100)
        driver.execute_script('document.querySelector("#lklq").dispatchEvent(new Event("mouseenter"));')
        driver.switch_to.default_content()

    def mouse_over_video_ok_ru(self, driver):
        import time
        time.sleep(5)
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_ok_ru(driver))

    def click_zingmp3_chon_giao_dien_btn(self, driver):
        if self.any_site_element.count_zingmp3_chon_giao_dien_button(driver) > 0:
            self.any_site_element.find_zingmp3_chon_giao_dien_button(driver).click()

