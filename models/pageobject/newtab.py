from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from models.pageelements.newtab import NewTabSearchElement, NewTabIconSitesElement, NewTabZenElements, \
    NewTabWidgetElements
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


class NewTabIconSitesPageObject(BasePageObject):

    new_tab_icon_site_elem = NewTabIconSitesElement()

    def get_total_number_most_visited_sites(self, driver):
        return len(self.new_tab_icon_site_elem.find_all_most_visited_sites(driver))

    def get_total_number_most_paid_sites(self, driver):
        return len(self.new_tab_icon_site_elem.find_all_most_paid_sites(driver))

    def get_attribute_any_most_visited_site_element(self, driver, nth_element, attribute_name):
        return self.new_tab_icon_site_elem.find_all_most_visited_sites(driver)[nth_element].get_attribute(attribute_name)

    def get_attribute_any_most_visited_paid_element(self, driver, nth_element, attribute_name):
        return self.new_tab_icon_site_elem.find_all_most_paid_sites(driver)[nth_element].get_attribute(attribute_name)

    def click_any_most_visited_site_element(self, driver, nth_element):
        self.new_tab_icon_site_elem.find_all_most_visited_sites(driver)[nth_element].click()

    def click_any_most_visited_paid_element(self, driver, nth_element):
        self.new_tab_icon_site_elem.find_all_most_paid_sites(driver)[nth_element].click()


class NewTabZenPageObject(BasePageObject):
    new_tab_zen_elem = NewTabZenElements()

    def click_on_any_zen_element(self, driver):
        driver.execute_script('arguments[0].click();', self.new_tab_zen_elem.find_any_zen_element(driver))

    def move_to_any_zen_element(self, driver):
        actions = ActionChains(driver)
        actions.move_to_element(self.new_tab_zen_elem.find_any_zen_element(driver)).perform()

    def get_attribute_any_zen_element(self, driver, attribute_name):
        return self.new_tab_zen_elem.find_any_zen_element(driver).get_attribute(attribute_name)

    def get_number_of_all_current_zen_elements(self, driver):
        return len(self.new_tab_zen_elem.find_all_current_zen_elements(driver))

    def get_attribute_all_zen_elements(self, driver, attribute_name):
        attribute_value = []
        for element in self.new_tab_zen_elem.find_all_current_zen_elements(driver):
            attribute_value.append(element.get_attribute(attribute_name))
        return attribute_value

    def get_attribute_all_zen_except_ads_elements(self, driver, attribute_name):
        attribute_value = []
        for element in self.new_tab_zen_elem.find_all_current_zen_except_ads_elements(driver):
            attribute_value.append(element.get_attribute(attribute_name))
        return attribute_value


class NewTabWidgetActions(BasePageObject):
    new_tab_widget_elem = NewTabWidgetElements()

    def click_on_widget_button(self, driver: WebDriver):
        element: WebElement = self.new_tab_widget_elem.find_edit_widget_button(driver=driver)
        element.click()

    def click_on_selected_widget(self, driver: WebDriver):
        element: WebElement = self.new_tab_widget_elem.find_selected_widget_element(driver=driver)
        element.click()

    def click_on_done_button(self, driver: WebDriver):
        element: WebElement = self.new_tab_widget_elem.find_done_widget_button(driver=driver)
        element.click()

    def get_attribute_selected_widget(self, driver: WebDriver):
        element: WebElement = self.new_tab_widget_elem.find_selected_background_image(driver=driver)
        return element.get_attribute('style')

    def click_on_reset_button(self, driver: WebDriver):
        element: WebElement = self.new_tab_widget_elem.find_reset_button_element(driver=driver)
        element.click()







