import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from models.pageelements.newtab import NewTabSearchElement, NewTabIconSitesElement, NewTabZenElements, \
    NewTabWidgetElements, NewTabAdsElements, NewTabLogAdsElements
from models.pageobject.basepage_object import BasePageObject

LOGGER = logging.getLogger(__name__)

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
        return self.new_tab_icon_site_elem.find_all_most_visited_sites(driver)[nth_element].get_attribute(
            attribute_name)

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


class NewTabAdsActions(BasePageObject):
    new_tab_ads_elem = NewTabAdsElements()

    def count_all_most_visited_ads(self, driver: WebDriver):
        return len(self.new_tab_ads_elem.find_all_most_visited_ads(driver))

    def click_on_most_visited_ads(self, driver: WebDriver, index):
        element: WebElement = self.new_tab_ads_elem.find_most_visited_ads_by_index(driver, index)
        element.click()

    def count_all_news(self, driver: WebDriver):
        return len(self.new_tab_ads_elem.find_all_news(driver))

    def count_all_news_ads(self, driver: WebDriver):
        return len(self.new_tab_ads_elem.find_all_news_ads(driver))


class NewTabLogAdsActions(BasePageObject):
    new_tab_log_ads_element = NewTabLogAdsElements()

    def switch_to_banner_ads_640x360_iframe(self, driver: WebDriver):
        LOGGER.info("Switch to video iframe")
        driver.switch_to.frame(self.new_tab_log_ads_element.find_banner_ads_640x360_iframe(driver))

    def click_on_banner_ads_640x360_ads(self, driver: WebDriver):
        LOGGER.info("Click on banner ads")
        self.new_tab_log_ads_element.find_banner_ads_640x360_ads(driver).click()

    def click_on_skin_ads(self, driver: WebDriver):
        LOGGER.info("Click skin ads")
        self.new_tab_log_ads_element.find_skin_ads(driver).click()

    def click_on_video_ads_close_float_button(self, driver: WebDriver):
        LOGGER.info("Click video ads and close float button")
        time.sleep(1)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        total_close_float_button = self.new_tab_log_ads_element.count_video_ads_close_float_button(driver)
        from datetime import datetime
        start_time = datetime.now()
        if total_close_float_button == 0:
            while total_close_float_button == 0:
                time.sleep(1)
                total_close_float_button = self.new_tab_log_ads_element.count_video_ads_close_float_button(driver)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= 5:
                    break
        self.new_tab_log_ads_element.find_video_ads_close_float_button(driver).click()

    def click_on_video_ads(self, driver: WebDriver):
        LOGGER.info("Click video ads")
        time.sleep(10)
        driver.switch_to.frame(self.new_tab_log_ads_element.find_video_ads_video_iframe(driver))
        self.new_tab_log_ads_element.find_video_ads_video(driver).click()

    def click_on_news_card(self, driver: WebDriver, news_type, is_right_click=False):
        LOGGER.info("Click "+news_type+" news")
        news_element = self.new_tab_log_ads_element.find_news_card(driver, news_type)
        if is_right_click is False:
            news_element.click()
        else:
            self.right_click_then_open_link_in_newtab(driver, news_element)

    def click_on_news_ads_card(self, driver: WebDriver, ads_type, is_right_click=False):
        LOGGER.info("Click " + ads_type + " ads")
        ads_element = self.new_tab_log_ads_element.find_news_ads_card(driver, ads_type)
        if is_right_click is False:
            ads_element.click()
        else:
            self.right_click_then_open_link_in_newtab(driver, ads_element)

    def click_on_news_custom_button(self, driver: WebDriver, news_type):
        LOGGER.info("Click news custom button")
        self.new_tab_log_ads_element.find_news_customs_button(driver, news_type).click()

    def click_on_news_action_button(self, driver: WebDriver, news_type, action):
        LOGGER.info("Click news "+action+" button ")
        if 'Big' in news_type:
            news_type = 'big'
        else:
            news_type = 'small'
        if action == 'like':
            self.new_tab_log_ads_element.find_news_action_button(driver, news_type, action).click()
        elif action == 'dislike':

            self.new_tab_log_ads_element.find_news_action_button(driver, news_type, action='like').click()
            self.new_tab_log_ads_element.find_news_action_button(driver, news_type, action).click()
        else:
            self.click_on_news_custom_button(driver, news_type)
            self.new_tab_log_ads_element.find_news_action_button(driver, news_type, action).click()

    def scroll_to_news_card(self, driver: WebDriver, news_type):
        LOGGER.info("Scroll to news card: "+news_type)
        news_element = self.new_tab_log_ads_element.find_news_card(driver, news_type)
        self.scroll_to_element(driver, news_element)

    def scroll_to_news_ads_card(self, driver: WebDriver, ads_type):
        LOGGER.info("Scroll to ads card: "+ads_type)
        ads_element = self.new_tab_log_ads_element.find_news_ads_card(driver, ads_type)
        self.scroll_to_element(driver, ads_element)