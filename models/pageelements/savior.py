import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.downloads import DownloadsPageLocators
from models.pagelocators.savior import SaviorPageLocators

LOGGER = logging.getLogger(__name__)


class SaviorElements(BasePageElement):
    script_query_all_two_layers = 'return document.querySelector(arguments[0]).' \
                                  'shadowRoot.querySelectorAll(arguments[1])'

    script_query_all_three_layers = 'return document.querySelector(arguments[0]).' \
                                    'shadowRoot.querySelector(arguments[1]).querySelectorAll(arguments[2])'

    def find_first_layer(self, driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, SaviorPageLocators.FIRST_LAYER)))

    def select_shadow_element_savior(self, driver, element1, element2):
        try:
            element = driver.execute_script(
                'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1])',
                element1, element2)
            return element
        except:
            return 1

    def select_shadow_element_savior_only_root(self, driver):
        return driver.execute_script('return document.querySelector(arguments[0]).shadowRoot', SaviorPageLocators.
                                     FIRST_LAYER)

    def select_shadow_element_download_button(self, driver):
        return self.select_shadow_element_savior(driver, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.
                                                 DOWNLOAD_BUTTON)

    def select_shadow_element_preferred_select(self, driver):
        return self.select_shadow_element_savior(driver, SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.
                                                 PREFERRED_SELECT_BTN)

    def find_download_button(self, driver):
        return self.select_shadow_element_download_button(driver)

    def not_found_download_button(self, driver):
        LOGGER.info('Value for assertions isssss:', self.select_shadow_element_download_button(driver))
        assert self.select_shadow_element_download_button(driver) in (1, None)

    def find_preferred_option(self, driver):
        try:
            return self.find_shadow_element(driver, SaviorPageLocators.FIRST_LAYER,
                                            SaviorPageLocators.PREFERRED_SELECT_BTN)
        # return self.select_shadow_element_by_css_selector(driver, self.find_first_layer(driver)). \
        #     find_element_by_css_selector(SaviorPageLocators.PREFERRED_SELECT_BTN)
        except:
            return None

    def find_resotion_option_by_css_selector(self, driver, css_selector):
        return self.find_shadow_element(driver, SaviorPageLocators.FIRST_LAYER, css_selector)

    def find_mobile_sharing_button(self, driver):
        return self.select_shadow_element_by_css_selector(driver, self.find_first_layer(driver)). \
            find_element_by_css_selector(SaviorPageLocators.MOBILE_SHARING_BUTTON)

    def find_all_subtitles(self, driver):
        return driver.execute_script(self.script_query_all_two_layers, SaviorPageLocators.FIRST_LAYER,
                                     SaviorPageLocators.SUBTITLE_ALL_SELECTOR)

    def find_all_video_options(self, driver):
        return driver.execute_script(self.script_query_all_three_layers, SaviorPageLocators.FIRST_LAYER,
                                     SaviorPageLocators.CLASS_WRAPPER_VIDEO_OPTIONS,
                                     SaviorPageLocators.ALL_VIDEO_OPTIONS_AVAILABLE)

    def get_current_video_quality_value(self, driver):
        return driver.execute_script('return document.querySelector(arguments[0]).shadowRoot.'
                                     'querySelector(arguments[1]).getAttribute("data-selected-value")',
                                     SaviorPageLocators.FIRST_LAYER, SaviorPageLocators.CURRENT_VIDEO_QUALITY_ITEM)

    def get_current_video_file_size(self, driver):
        return driver.execute_script('document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).'
                                     'querySelector(arguments[2]).textContent',
                                     SaviorPageLocators.FIRST_LAYER,
                                     SaviorPageLocators.CURRENT_VIDEO_QUALITY_SELECTED_ITEM,
                                     SaviorPageLocators.CURRENT_VIDEO_FILE_SIZE_ITEM)

    def get_each_quality_info_video_options(self, driver, i):
        return driver.execute_script('return document.querySelector(arguments[0]).'
                                     'shadowRoot.querySelector(arguments[1]).'
                                     'querySelectorAll(arguments[2])[arguments[3]].'
                                     'getAttribute("data-quality-value")', SaviorPageLocators.FIRST_LAYER,
                                     SaviorPageLocators.CLASS_WRAPPER_VIDEO_OPTIONS,
                                     SaviorPageLocators.ALL_VIDEO_OPTIONS_AVAILABLE, i)

    def find_play_button_by_video_title(self, driver, video_title):
        play_button_xpath = DownloadsPageLocators.PLAY_BUTTON_BY_VIDEO_TITLE.replace('{param1}', video_title)
        play_button_element = self.find_element_if_exist(driver, (By.XPATH, play_button_xpath))
        return play_button_element

    def get_savior_wigdet_choose_resolution_status(self, driver):
        choose_resolution_status = driver.execute_script(
            'return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]).'
            'textContent', SaviorPageLocators.FIRST_LAYER,
            SaviorPageLocators.SAVIOR_WIGDET_DONE_SPAN_CSS)
        LOGGER.info("Choose resolution status: " + str(choose_resolution_status))
        return str(choose_resolution_status)
