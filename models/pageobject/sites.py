import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from models.pageelements.sites import YoutubePageElements, GooglePageElements
from models.pageobject.basepage_object import BasePageObject


class YoutubePageObject(BasePageObject):
    youtube_element = YoutubePageElements()

    def choose_any_video_item(self, driver):
        profile_path_elem = self.youtube_element.find_any_video_item(driver)
        return profile_path_elem.get_attribute('href')

    def mouse_over_video_item(self, driver):
        video_element = self.youtube_element.find_video_player_item(driver)
        hov = ActionChains(driver).move_to_element(video_element)
        hov.perform()
        time.sleep(2)

    def click_video_item(self, driver):
        self.youtube_element.find_video_player_item(driver).click()


class GooglePageObject(BasePageObject):
    google_element = GooglePageElements()

    def search_with_value(self, driver, text_value):
        search_field = self.google_element.find_search_field(driver)
        search_field.click()
        search_field.send_keys(text_value)
        search_field.send_keys(Keys.RETURN)
        time.sleep(4)

    def search_result_video(self, driver):
        self.google_element.find_video_search_btn(driver).click()

    def download_via_savior_icon_button(self, driver):
        self.google_element.find_savior_icon(driver).click()

