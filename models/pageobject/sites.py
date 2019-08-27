import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from models.pageelements.sites import YoutubePageElements, GooglePageElements, AnySiteElements
from models.pageobject.basepage_object import BasePageObject
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
        while BasePageObject.verify_savior_popup_appear(driver) is None:
            any_video_element = self.any_site_element.find_first_video_element(driver)
            hov = ActionChains(driver).move_to_element(any_video_element)
            hov.perform()

    def click_first_video_element(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        self.any_site_element.click_first_video_element(driver)

    def click_video_element_24h(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        self.any_site_element.find_video_element_24h(driver).click()

    def mouse_over_video_element_24h(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        while BasePageObject.verify_savior_popup_appear(driver) is None:
            hov = ActionChains(driver).move_to_element(self.any_site_element.find_video_element_24h(driver))
            hov.perform()

    def click_video_element_phimmoi(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        self.any_site_element.find_video_element_phimmoi(driver).click()

    def mouse_over_video_element_phimmoi(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        hov = ActionChains(driver).move_to_element(self.any_site_element.find_video_element_phimmoi(driver))
        hov.perform()

    def close_popup_continue_watching(self, driver):
        WaitAfterEach.sleep_timer_after_each_step()
        self.any_site_element.find_close_popup_continue_watching(driver).click()

    def mouse_over_video_element_facebook(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        while BasePageObject.verify_savior_popup_appear(driver) is None:
            hov = ActionChains(driver).move_to_element(self.any_site_element.find_video_item_in_facebook_page(driver))
            hov.perform()

    def mouse_over_video_element_messenger_chat(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        while BasePageObject.verify_savior_popup_appear(driver) is None:
            hov = ActionChains(driver).move_to_element(self.any_site_element.find_video_item_in_messenger_chat(driver))
            hov.perform()

    def click_video_element_messenger_chat(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        self.any_site_element.click_video_item_in_messenger_chat(driver)

    def mouse_over_video_element_instagram(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        while BasePageObject.verify_savior_popup_appear(driver) is None:
            hov = ActionChains(driver).move_to_element(self.any_site_element.find_video_item_in_instagram(driver))
            hov.perform()

    def mouse_over_video_item_kienthuc(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        while BasePageObject.verify_savior_popup_appear(driver) is None:
            hov = ActionChains(driver).move_to_element(self.any_site_element.find_video_item_in_kienthuc(driver))
            hov.perform()

    def click_video_item_kienthuc(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        self.any_site_element.find_video_item_in_kienthuc(driver).click()

    def mouse_over_video_item_vietnamnet(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        while BasePageObject.verify_savior_popup_appear(driver) is None:
            hov = ActionChains(driver).move_to_element(self.any_site_element.find_video_item_vietnamnet(driver))
            hov.perform()

    def mouse_over_video_item_eva_vn(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        while BasePageObject.verify_savior_popup_appear(driver) is None:
            hov = ActionChains(driver).move_to_element(self.any_site_element.find_video_item_eva_vn(driver))
            hov.perform()

    def mouse_over_video_item_twitter(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        while BasePageObject.verify_savior_popup_appear(driver) is None:
            hov = ActionChains(driver).move_to_element(self.any_site_element.find_video_item_twitter(driver))
            hov.perform()

    def mouse_over_video_item_soha(self, driver):
        WaitAfterEach.sleep_timer_after_each_step_longer_load()
        while BasePageObject.verify_savior_popup_appear(driver) is None:
            hov = ActionChains(driver).move_to_element(self.any_site_element.find_video_item_soha(driver))
            hov.perform()




