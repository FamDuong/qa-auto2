from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from models.pageelements.top_savior_sites.top_savior_sites_film import TopSaviorSitesFilmElements
from models.pageobject.basepage_object import BasePageObject


class TopSaviorSitesFilmActions(BasePageObject):

    top_savior_sites_film_element = TopSaviorSitesFilmElements()

    def close_login_popup_tv_zing(self, driver: WebDriver):
        element: WebElement
        element = self.top_savior_sites_film_element.find_close_login_popup_element_button(driver)
        element.click()

    def close_popup_ad_if_appear(self, driver: WebDriver):
        elements = self.top_savior_sites_film_element.find_close_button_phimmoi_ad(driver)
        if len(elements) == 1:
            elements[0].click()
        else:
            pass

