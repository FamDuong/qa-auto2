from selenium.webdriver import ActionChains

from models.pageelements.youtube import YoutubePageElements
from models.pageobject.basepage_object import BasePageObject


class YoutubePageObject(BasePageObject):
    youtube_element = YoutubePageElements()

    def choose_any_video_item(self, driver):
        profile_path_elem = self.youtube_element.find_any_video_item(driver)
        profile_path_elem.click()

    def mouse_over_video_item(self, driver):
        video_element = self.youtube_element.find_video_player_item(driver)
        hov = ActionChains(driver).move_to_element(video_element)
        hov.perform()
        video_element.click()


