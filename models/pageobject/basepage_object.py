import time
import logging
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from models.pagelocators.savior import SaviorPageLocators
from models.pageelements.version import VersionPageElements
from utils_automation.common import WebElements
from selenium.webdriver.support.wait import WebDriverWait
from utils_automation.setup import WaitAfterEach
import re

LOGGER = logging.getLogger(__name__)


class BasePageObject(object):
    version_element = VersionPageElements()

    def wait_until_document_ready(self, driver):
        wait_document_ready = WebDriverWait(driver, 60)
        wait_document_ready.until(lambda driver1: driver.execute_script("return document.readyState") == "complete")

    def send_keys_to_element(self, driver, element, keys):
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys(keys)
        actions.perform()

    def clear_text_to_element(self, driver, element):
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click()
        actions.key_down(Keys.CONTROL)
        actions.send_keys("a")
        actions.key_up(Keys.CONTROL)
        actions.send_keys(Keys.DELETE)
        actions.perform()

    def get_text_element(self, element):
        return element.get_attribute('textContent')

    def get_text_element_by_id(self, driver, locator):
        element = self.version_element.find_element(driver, locator)
        return element.text

    def press_arrow_up(self, driver, loop=1):
        for i in range(loop):
            driver.find_element_by_css_selector('body').send_keys(Keys.ARROW_UP)
            WaitAfterEach.sleep_timer_after_each_step()

    def verify_savior_popup_appear(self, driver, timeout=3):

        def find_download_button():
            return driver.execute_script('return document.querySelector(arguments[0]).'
                                         'shadowRoot.querySelector(arguments[1])', SaviorPageLocators.FIRST_LAYER,
                                         SaviorPageLocators.DOWNLOAD_BUTTON)

        start_time = datetime.now()
        while self.get_element_first_layer_savior(driver) is None:
            time.sleep(1)
            time_delta = datetime.now() - start_time
            if time_delta.total_seconds() >= timeout:
                break
        try:
            if self.get_element_first_layer_savior(driver) is not None:
                a = find_download_button()
                return a
        except StaleElementReferenceException as e:
            LOGGER.info(e)

    def get_element_first_layer_savior(self, driver):
        return driver.execute_script('return document.querySelector(arguments[0])', SaviorPageLocators.FIRST_LAYER)

    def mouse_over_video_element_site(self, driver, element, timeout=12, timeout_verify_savior_popup=4):
        start_time = datetime.now()
        while self.verify_savior_popup_appear(driver, timeout=timeout_verify_savior_popup) is None:
            try:
                WebElements.mouse_over_element(driver, element)
                time_delta = datetime.now() - start_time
                if time_delta.total_seconds() >= timeout:
                    break
            except StaleElementReferenceException as e:
                LOGGER.info(e)

    def verify_text_is_visible_on_page(self, driver, component_name):
        # assert self.settings_elem.find_components_by_name(driver, component_name) == 1
        src = driver.page_source
        text_found = re.search(component_name, src)
        assert text_found is not None

    def choose_drop_down_value_js(self, driver, element, option_index):
        driver.execute_script('arguments[0].options[arguments[1]].selected = true;', element, option_index)

    def click_on_element_if_exist(self, element):
        i = 0
        try:
            if element is not None:
                while i == 0:
                    element.click()
                    i += 1
        except NoSuchElementException as e:
            LOGGER.info(e.stacktrace)
        except ElementClickInterceptedException as intercepted:
            LOGGER.info(intercepted.stacktrace)

    def scroll_to_with_scroll_height(self, driver):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_to_element(self, driver, element):
        driver.execute_script('arguments[0].scrollIntoView()', element)

    def right_click_then_open_link_in_newtab(self, driver, element):
        ActionChains(driver).context_click(element).key_down(Keys.CONTROL).click(element).perform()

