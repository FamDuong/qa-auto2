from selenium.webdriver.chrome.webdriver import WebDriver
from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec
from models.pagelocators.top_savior_sites.top_savior_sites_news import TopSaviorSitesNewsLocators


class TopSaviorSitesNewsElements(BasePageElement):

    def find_zing_news_play_video_button(self, driver: WebDriver):
        return self.find_element_if_exist(driver, TopSaviorSitesNewsLocators.ZING_NEWS_PLAY_VIDEO_BTN)

    def count_zing_news_play_video_button(self, driver: WebDriver):
        element = driver.find_elements_by_css_selector(TopSaviorSitesNewsLocators.ZING_NEWS_PLAY_VIDEO_BTN_CSS)
        return len(element)

    def find_vietnamnet_video_iframe(self, driver, iframe):
        return self.find_element_if_exist(driver, iframe)

    def find_vietnamnet_video(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(TopSaviorSitesNewsLocators.VIETNAMNET_VIDEO))

