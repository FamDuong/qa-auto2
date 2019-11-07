import random

from models.pageelements.newtab import NewTabSearchElement
from models.pageobject.basepage_object import BasePageObject


class NewTabSearchPageObject(BasePageObject):

    new_tab_search_element = NewTabSearchElement()

    def get_css_value_search_string_element(self, driver, css_property):
        return self.new_tab_search_element.find_search_string_element(driver).value_of_css_property(css_property)

    def send_key_string_to_search_string_element(self, driver, *text):
        return self.new_tab_search_element.find_search_string_element(driver).send_keys(text)

    def get_css_value_search_button_element(self, driver, css_property):
        return self.new_tab_search_element.find_search_button_element(driver).value_of_css_property(css_property)

    def click_search_button_element(self, driver):
        return self.new_tab_search_element.find_search_button_element(driver).click()

    def get_total_number_most_visited_sites(self, driver):
        return len(self.new_tab_search_element.find_all_most_visited_sites(driver))

    def get_attribute_any_most_visited_site_element(self, driver, nth_element, attribute_name):
        return self.new_tab_search_element.find_all_most_visited_sites(driver)[nth_element].get_attribute(attribute_name)

    def click_any_most_visited_site_element(self, driver, nth_element):
        self.new_tab_search_element.find_all_most_visited_sites(driver)[nth_element].click()







