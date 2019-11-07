from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec
from models.pagelocators.newtab import NewTabSearchLocators


class NewTabSearchElement(BasePageElement):

    def find_search_string_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabSearchLocators.SEARCH_STRING))

    def find_search_button_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabSearchLocators.SEARCH_BUTTON))

    def find_all_most_visited_sites(self, driver):
        self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabSearchLocators.MOST_VISITED_TITLES))
        return driver.find_elements_by_css_selector(NewTabSearchLocators.MOST_VISITED_TITLES_CSS_SELECTOR)














