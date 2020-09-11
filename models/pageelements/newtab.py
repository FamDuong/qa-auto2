from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec
from models.pagelocators.newtab import NewTabSearchLocators, NewTabIconSitesLocators, NewTabZenLocators, \
    NewTabWidgetLocators, NewTabMostVisitedLocators


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

    def find_all_current_zen_except_ads_elements(self, driver):
        self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabZenLocators
                                                                           .ZEN_NEWS_NOT_CONTAINS_ADS_ITEM))
        return driver.find_elements_by_css_selector(NewTabZenLocators.ZEN_NEWS_NOT_CONTAINS_ADS_ITEM_CSS_SELECTOR)


class NewTabWidgetElements(BasePageElement):
    def find_edit_widget_button(self, driver: WebDriver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(NewTabWidgetLocators.EDIT_WIDGET_BUTTON))

    def find_selected_widget_element(self, driver: WebDriver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabWidgetLocators.SELECTED_WIDGET))

    def find_selected_background_image(self, driver: WebDriver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(NewTabWidgetLocators.SELECTED_BACKGROUND_IMAGE))

    def find_done_widget_button(self, driver: WebDriver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(NewTabWidgetLocators.DONE_BUTTON))

    def find_reset_button_element(self, driver: WebDriver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(NewTabWidgetLocators.RESET_DEFAULT_BUTTON))


class NewTabAdsElements(BasePageElement):
    def find_all_most_visited_ads(self, driver: WebDriver):
        self.find_element_if_exist(driver, NewTabMostVisitedLocators.TOTAL_MOST_VISITED_QC)
        return driver.find_elements_by_xpath(NewTabMostVisitedLocators.TOTAL_MOST_VISITED_QC_XPATH)

    def find_all_news(self, driver: WebDriver):
        self.find_element_if_exist(driver, NewTabMostVisitedLocators.TOTAL_MOST_VISITED_QC)
        return driver.find_elements_by_xpath(NewTabMostVisitedLocators.TOTAL_NEWS_XPATH)

    def find_all_news_ads(self, driver: WebDriver):
        self.find_element_if_exist(driver, NewTabMostVisitedLocators.TOTAL_MOST_VISITED_QC)
        return driver.find_elements_by_xpath(NewTabMostVisitedLocators.TOTAL_NEWS_ADS_XPATH)