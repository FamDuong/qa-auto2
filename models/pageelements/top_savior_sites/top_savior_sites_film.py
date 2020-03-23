from selenium.webdriver.chrome.webdriver import WebDriver

from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec

from models.pagelocators.top_savior_sites.top_savior_sites_film import TopSaviorSitesFilmLocators


class TopSaviorSitesFilmElements(BasePageElement):

    def find_close_login_popup_element_button(self, driver: WebDriver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(TopSaviorSitesFilmLocators
                                                                                  .TV_ZING_VN_CLOSE_LOGIN_POPUP_LOCATOR))
