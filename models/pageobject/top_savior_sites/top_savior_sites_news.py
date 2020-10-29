from selenium.webdriver.chrome.webdriver import WebDriver
from models.pageelements.top_savior_sites.top_savior_sites_news import TopSaviorSitesNewsElements
from models.pageobject.basepage_object import BasePageObject


class TopSaviorSitesNewsActions(BasePageObject):
    top_savior_sites_news_element = TopSaviorSitesNewsElements()

    def click_vtc_play_video_button(self, driver: WebDriver):
        element = self.top_savior_sites_news_element.find_vtc_play_video_button(driver)
        element.click()

    def click_zing_news_play_video_button(self, driver: WebDriver):
        if self.top_savior_sites_news_element.count_zing_news_play_video_button(driver) > 0:
            element = self.top_savior_sites_news_element.find_zing_news_play_video_button(driver)
            element.click()

    def switch_to_vietnamnet_video_iframe(self, driver, iframe):
        driver.switch_to.frame(self.top_savior_sites_news_element.find_vietnamnet_video_iframe(driver, iframe))

    def mouse_over_vietnamnet_video(self, driver, iframe):
        self.mouse_over_video_element_site(driver, self.top_savior_sites_news_element.find_vietnamnet_video_iframe(driver, iframe))
