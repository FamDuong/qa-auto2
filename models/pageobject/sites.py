import time
from datetime import datetime
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from models.pageelements.sites import YoutubePageElements, GooglePageElements, AnySiteElements
from models.pagelocators.sites import AnySite
from models.pageobject.basepage_object import BasePageObject
from utils_automation.common import WebElements
from utils_automation.setup import WaitAfterEach


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
        video_element = self.youtube_element.find_video_player_item(driver)
        hov = ActionChains(driver).move_to_element(video_element)
        hov.perform()
        WaitAfterEach.sleep_timer_after_each_step()

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
            driver.switch_to.default_content()
            args
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= time_out_sec:
                break

    def mouse_over_video_iframe_with_minimize_maximize(self, driver, switch_to_iframe_video, find_video_item,
                                                       time_out_sec):
        self.mouse_over_video_iframe(driver, switch_to_iframe_video, find_video_item, time_out_sec,
                                     driver.maximize_window(),
                                     driver.minimize_window())

    def mouse_over_first_video_element(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_first_video_element(driver))

    def click_first_video_element(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        self.any_site_element.click_first_video_element(driver)

    def click_video_element_24h(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        self.any_site_element.find_video_element_24h(driver).click()

    def mouse_over_video_element_24h(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_element_24h(driver))

    def mouse_over_video_element_phimmoi(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_element_mouse_over_phimmoi(driver))

    def verify_exist_ads_pop_up_phim_moi(self, driver):
        return len(self.any_site_element.find_elements_close_pop_up_ads_phim_moi(driver))

    def close_popup_continue_watching(self, driver):
        WaitAfterEach.sleep_timer_after_each_step()
        self.any_site_element.find_close_popup_continue_watching(driver).click()

    def close_image_popup_phim_moi(self, driver):
        self.any_site_element.find_close_image_popup_phim_moi(driver).click()

    def mouse_over_video_element_facebook(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_in_facebook_page(driver))

    def mouse_over_video_element_messenger_chat(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_in_messenger_chat(driver))

    def click_video_element_messenger_chat(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        self.any_site_element.click_video_item_in_messenger_chat(driver)

    def mouse_over_video_element_instagram(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_in_instagram(driver))

    def mouse_over_video_item_kienthuc(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_in_kienthuc(driver))

    def click_video_item_kienthuc(self, driver):
        ActionChains(driver).move_to_element(self.any_site_element.find_video_item_in_kienthuc(driver)).perform()
        self.any_site_element.find_video_item_in_kienthuc(driver).click()

    def mouse_over_video_item_vietnamnet(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_vietnamnet(driver))

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
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_2sao_vn(driver))

    def mouse_over_video_item_phunu_giadinh(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_phunu_giadinh(driver))

    def click_video_item_phunu_giadinh(self, driver):
        self.any_site_element.find_video_item_phunu_giadinh(driver).click()

    def switch_to_iframe_tien_phong(self, driver):
        driver.switch_to.frame(self.any_site_element.find_iframe_tien_phong(driver))

    def mouse_over_video_item_tien_phong(self, driver):
        self.mouse_over_video_iframe_with_minimize_maximize(driver, self.switch_to_iframe_tien_phong,
                                                            self.any_site_element.find_play_video_item_tien_phong,
                                                            10)

    def click_video_item_tien_phong(self, driver):
        self.switch_to_iframe_tien_phong(driver)
        ActionChains(driver).move_to_element(self.any_site_element.find_video_item_tien_phong(driver)).perform()
        self.any_site_element.find_video_item_tien_phong(driver).click()

    def switch_to_iframe_bong_da_dot_com(self, driver):
        driver.switch_to.frame(self.any_site_element.find_iframe_bong_da_dot_com(driver))

    def mouse_over_video_item_bong_da_dot_com(self, driver):
        self.mouse_over_video_iframe(driver, self.switch_to_iframe_bong_da_dot_com,
                                     self.any_site_element.find_video_item_bong_da_dot_com,
                                     20)

    def click_video_item_bong_da_dot_com(self, driver):
        self.switch_to_iframe_bong_da_dot_com(driver)
        ActionChains(driver).move_to_element(self.any_site_element.find_video_item_bong_da_dot_com(driver)).perform()
        self.any_site_element.find_video_item_bong_da_dot_com(driver).click()

    def mouse_over_video_item_gia_dinh_dot_net(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_gia_dinh_dot_net(driver))

    def mouse_over_video_item_a_family(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_a_family(driver))

    def mouse_over_video_item_gamek_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_gamek_vn(driver))

    def switch_to_iframe_vu_vi_phim(self, driver):
        driver.switch_to.frame(self.any_site_element.find_iframe_vu_vi_phim(driver))

    def mouse_over_video_item_vu_vi_phim_maximize_minimize(self, driver):
        self.mouse_over_video_iframe_with_minimize_maximize(driver, self.switch_to_iframe_vu_vi_phim,
                                                            self.any_site_element.find_video_item_vu_vi_phim,
                                                            40)

    def click_video_item_vu_vi_phim(self, driver):
        self.switch_to_iframe_vu_vi_phim(driver)
        ActionChains(driver).move_to_element(self.any_site_element.find_video_item_vu_vi_phim(driver)).perform()
        self.any_site_element.find_video_item_vu_vi_phim(driver).click()

    def double_click_video_item_vu_vi_phim(self, driver):
        self.switch_to_iframe_vu_vi_phim(driver)
        ActionChains(driver).move_to_element(
            self.any_site_element.find_video_item_vu_vi_phim(driver)).double_click().perform()

    def click_full_screen_vu_vi_phim(self, driver):
        ActionChains(driver).move_to_element(self.any_site_element.find_full_screen_button_vu_vi_phim(driver)).perform()
        self.any_site_element.find_full_screen_button_vu_vi_phim(driver).click()

    def click_video_item_an_ninh_thu_do(self, driver):
        self.any_site_element.find_video_item_an_ninh_thu_do(driver).click()

    def mouse_over_video_item_an_ninh_thu_do(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_an_ninh_thu_do(driver))

    def mouse_over_video_item_tuoi_tre(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_tuoi_tre(driver))

    def click_video_item_mot_phim(self, driver):
        ActionChains(driver).move_to_element(
            self.any_site_element.find_play_button_video_mot_phim(driver)).click().perform()

    def click_video_episode_mot_phim(self, driver):
        self.any_site_element.find_video_episode_mot_phim(driver).click()

    def click_video_box_player_mot_phim(self, driver):
        self.any_site_element.find_video_box_player_mot_phim(driver).click()

    def mouse_over_video_item_mot_phim(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_mot_phim(driver))

    def skip_ads_tv_hay(self, driver):
        self.any_site_element.find_skip_ads_btn_tv_hay(driver).click()

    def click_play_btn_tv_hay(self, driver):
        self.any_site_element.find_play_btn_tv_hay(driver).click()

    def mouse_over_video_item_tv_hay(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_tv_hay(driver))

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

    def mouse_over_video_vn_express(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_vn_express(driver))

    def mouse_over_video_thanh_nien_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_thanh_nien(driver))

    def mouse_over_video_dan_tri_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_dan_tri_vn(driver))

    def mouse_over_video_nguoi_lao_dong_tv(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_nguoi_lao_dong_tv(driver))

    def click_video_anime_vsub_tv(self, driver):
        self.any_site_element.find_video_item_anime_sub_tv(driver).click()

    def mouse_over_video_anime_vsub_tv(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_anime_sub_tv(driver))

    def choose_continue_from_start_anime_subtv(self, driver):
        self.any_site_element.find_continue_from_start_popup_btn_anime_sub_tv(driver).click()

    def close_and_watch_ad_button_anime_subtv(self, driver):
        self.any_site_element.find_close_ad_btn_anime_vsub_tv(driver).click()

    def mouse_over_video_nhac_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_nhac_vn(driver))

    def mouse_over_video_x_videos(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_xvideos(driver))

    def mouse_over_video_xnxx(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_xnxx(driver))

    def mouse_over_video_fr_porn_hub(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_fr_porn_hub(driver))

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
        self.any_site_element.find_video_wrapper_phim_sex_porn(driver).click()

    def mouse_over_video_phim_sex_porn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_phim_sex_porn_item(driver))

    def click_video_jav_phim(self, driver):
        self.any_site_element.find_video_phim_jav_phim_wrapper(driver).click()

    def mouse_over_video_jav_phim(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_phim_jav_phim_item(driver))

    def mouse_over_video_tin_moi(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_tin_moi(driver))

    def mouse_over_video_info_net(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_info_net(driver))

    def mouse_over_video_bong_da_24h(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_bong_da_24h(driver))

    def click_video_item_keo_nha_cai(self, driver):
        self.any_site_element.find_video_item_keo_nha_cai(driver).click()

    def mouse_over_video_item_keo_nha_cai(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_keo_nha_cai(driver))

    def mouse_over_video_item_daily_motion(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_daily_motion(driver))

    def switch_to_frame_vov_vn(self, driver):
        driver.switch_to.frame(self.any_site_element.find_video_vov_vn_iframe(driver))

    def mouse_over_video_item_vov_vn_maximize_minimize(self, driver):
        self.mouse_over_video_iframe_with_minimize_maximize(driver, self.switch_to_frame_vov_vn,
                                                            self.any_site_element.find_video_vov_vn,
                                                            20)
        driver.switch_to.default_content()

    def click_video_item_vov_vn(self, driver):
        self.any_site_element.find_video_vov_vn_iframe(driver).click()

    def mouse_over_video_element_sex_ngon(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_sex_ngon(driver))

    def click_video_element_sex_ngon(self, driver):
        self.any_site_element.find_video_sex_ngon(driver).click()

    def mouse_over_video_element_weibo(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_weibo(driver))

    def choose_server_anime_tvn(self, driver, server_number):
        self.any_site_element.find_server_anime_tvn(driver, server_number).click()

    def mouse_over_tvn_video_element(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_anime_tvn(driver))

    def mouse_over_phim_bat_hu_video_element(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_phim_bat_hu(driver))

    def click_video_phim_bat_hu_video_element(self, driver):
        self.any_site_element.find_video_phim_bat_hu_play(driver).click()

    def click_video_phim_sex_sub_video_element(self, driver):
        self.any_site_element.find_video_phim_sex_sub_wrapper(driver).click()

    def mouse_over_video_element_phim_sex_sub(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_phim_sex_sub_element(driver))

    def mouse_over_video_element_vlive_tv(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_vlive_tv_item(driver))

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
        self.any_site_element.find_video_player_doi_song_phap_luat(driver).click()
        while self.verify_savior_popup_appear(driver) is None:
            WaitAfterEach.sleep_timer_after_each_step()

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

    def click_video_item_dong_phim(self, driver):
        self.any_site_element.find_dong_phim_play_video_item(driver).click()
        WaitAfterEach.sleep_timer_after_each_step()










