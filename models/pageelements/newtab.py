from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec
from models.pagelocators.newtab import NewTabSearchLocators, NewTabIconSitesLocators, NewTabZenLocators


class NewTabSearchElement(BasePageElement):

    def find_search_string_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabSearchLocators.SEARCH_STRING))

    def find_search_button_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabSearchLocators.SEARCH_BUTTON))


class NewTabIconSitesElement(BasePageElement):
    def find_all_most_visited_sites(self, driver):
        self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabIconSitesLocators.MOST_VISITED_TITLES))
        return driver.find_elements_by_css_selector(NewTabIconSitesLocators.MOST_VISITED_TITLES_CSS_SELECTOR)

    def find_all_most_paid_sites(self, driver):
        self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabIconSitesLocators.MOST_VISITED_ICONS))
        return driver.find_elements_by_css_selector(NewTabIconSitesLocators.MOST_VISITED_ICONS_CSS_SELECTOR)


class NewTabZenElements(BasePageElement):
    def find_any_zen_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabZenLocators.ZEN_NEWS_ITEM))

    def find_all_current_zen_elements(self, driver):
        self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabZenLocators.ZEN_NEWS_ITEM))
        return driver.find_elements_by_css_selector(NewTabZenLocators.ZEN_NEWS_ITEM_CSS_SELECTOR)
















