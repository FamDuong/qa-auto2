from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.youtube import YoutubePageLocators


class YoutubePageElements(BasePageElement):

    def find_any_video_item(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located(YoutubePageLocators.ANY_VIDEO_ITEM))

    def find_video_player_item(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(
            ec.presence_of_element_located(YoutubePageLocators.VIDEO_PLAYER_ITEM))
