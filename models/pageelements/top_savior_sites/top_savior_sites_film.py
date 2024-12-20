from selenium.webdriver.chrome.webdriver import WebDriver
from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec
from models.pagelocators.top_savior_sites.top_savior_sites_film import TopSaviorSitesFilmLocators


class TopSaviorSitesFilmElements(BasePageElement):

    def find_close_button_phimmoi_ad_element(self, driver: WebDriver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesFilmLocators
                                                                                  .PHIMMOI_CLOSE_POPUP_LOCATOR))

    def find_close_button_phimmoi_ad(self, driver: WebDriver):
        return driver.find_elements_by_xpath(TopSaviorSitesFilmLocators.PHIMMOI_CLOSE_POPUP_LOCATOR_BY_XPATH)

    def find_film_index1_in_phimmoi(self, driver: WebDriver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesFilmLocators
                                                                                  .PHIMMOI_XEM_PHIM_BTN))
