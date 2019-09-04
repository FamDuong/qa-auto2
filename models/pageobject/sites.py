
import time
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from models.pageelements.sites import YoutubePageElements, GooglePageElements, AnySiteElements
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

    def click_video_element_phimmoi(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        self.any_site_element.find_video_element_phimmoi(driver).click()

    def mouse_over_video_element_phimmoi(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_element_phimmoi(driver))

    def close_popup_continue_watching(self, driver):
        WaitAfterEach.sleep_timer_after_each_step()
        self.any_site_element.find_close_popup_continue_watching(driver).click()

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

    def mouse_over_video_item_twitter(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_twitter(driver))

    def mouse_over_video_item_soha(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_soha(driver))

    def mouse_over_video_item_sao_2_vn(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_2sao_vn(driver))

    def choose_watch_from_beginning_fpt_play(self, driver):
        self.any_site_element.find_watch_beginning_fpt_play(driver).click()

    def mouse_over_video_item_fpt_play(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_fpt_play(driver))

    def mouse_over_video_item_phunu_giadinh(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_phunu_giadinh(driver))

    def click_video_item_phunu_giadinh(self, driver):
        self.any_site_element.find_video_item_phunu_giadinh(driver).click()

    def switch_to_iframe_tien_phong(self, driver):
        driver.switch_to.frame(self.any_site_element.find_iframe_tien_phong(driver))

    def mouse_over_video_item_tien_phong(self, driver):
        start_time = datetime.now()
        driver.switch_to.default_content()
        while self.verify_savior_popup_appear(driver) is None:
            self.switch_to_iframe_tien_phong(driver)
            WebElements.mouse_over_element(driver, self.any_site_element.find_play_video_item_tien_phong(driver))
            driver.switch_to.default_content()
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 1:
                break

    def click_video_item_tien_phong(self, driver):
        self.switch_to_iframe_tien_phong(driver)
        ActionChains(driver).move_to_element(self.any_site_element.find_video_item_tien_phong(driver)).perform()
        self.any_site_element.find_video_item_tien_phong(driver).click()

    def switch_to_iframe_bong_da_dot_com(self, driver):
        driver.switch_to.frame(self.any_site_element.find_iframe_bong_da_dot_com(driver))

    def mouse_over_video_item_bong_da_dot_com(self, driver):
        start_time = datetime.now()
        driver.switch_to.default_content()
        while self.verify_savior_popup_appear(driver) is None:
            self.switch_to_iframe_bong_da_dot_com(driver)
            WebElements.mouse_over_element(driver, self.any_site_element.find_video_item_bong_da_dot_com(driver))
            driver.switch_to.default_content()
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 20:
                break

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

    def mouse_over_video_item_vu_vi_phim(self, driver):
        start_time = datetime.now()
        driver.switch_to.default_content()
        while self.verify_savior_popup_appear(driver) is None:
            self.switch_to_iframe_vu_vi_phim(driver)
            WebElements.mouse_over_element(driver, self.any_site_element.find_video_item_vu_vi_phim(driver))
            driver.switch_to.default_content()
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= 40:
                break
        # self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_vu_vi_phim(driver))

    def click_video_item_vu_vi_phim(self, driver):
        self.switch_to_iframe_vu_vi_phim(driver)
        ActionChains(driver).move_to_element(self.any_site_element.find_video_item_vu_vi_phim(driver)).perform()
        self.any_site_element.find_video_item_vu_vi_phim(driver).click()

    def double_click_video_item_vu_vi_phim(self, driver):
        self.switch_to_iframe_vu_vi_phim(driver)
        ActionChains(driver).move_to_element(self.any_site_element.find_video_item_vu_vi_phim(driver)).double_click().perform()

    def click_full_screen_vu_vi_phim(self, driver):
        ActionChains(driver).move_to_element(self.any_site_element.find_full_screen_button_vu_vi_phim(driver)).perform()
        self.any_site_element.find_full_screen_button_vu_vi_phim(driver).click()

    def click_video_item_an_ninh_thu_do(self, driver):
        self.any_site_element.find_video_item_an_ninh_thu_do(driver).click()

    def mouse_over_video_item_an_ninh_thu_do(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_an_ninh_thu_do(driver))

    def mouse_over_video_item_tuoi_tre(self, driver):
        self.mouse_over_video_element_site(driver, self.any_site_element.find_video_item_tuoi_tre(driver))


