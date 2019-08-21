from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utils_automation.setup import WaitAfterEach
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.mojichat import MojichatLocators
from utils_automation.setup import WaitAfterEach

class BasePageObject(object):
    # def find_element(self, *locator):
    #     if locator.__len__() == 2:
    #         return self.driver.find_element(*locator)
    #     return self.driver.find_element(*(locator[1], locator[2] % locator[0]))
    #
    # def find_elements(self, *locator):
    #     if locator.__len__() == 2:
    #         return self.driver.find_elements(*locator)
    #     return self.driver.find_elements(*(locator[1], locator[2] % locator[0]))

    def wait_until_document_ready(self, driver):
        wait_document_ready = WebDriverWait(driver, 60)
        wait_document_ready.until(lambda driver1: driver.execute_script("return document.readyState") == "complete")

    def send_keys_to_element(self, driver, element, keys):
        actions = ActionChains(driver)
        actions.move_to_element(element);
        actions.click();
        actions.send_keys(keys);
        actions.perform()

    def clear_text_to_element(self, driver, element):
        actions = ActionChains(driver)
        actions.move_to_element(element);
        actions.click();
        actions.send_keys(Keys.CONTROL + "a");
        actions.send_keys(Keys.DELETE);
        actions.perform()

    def get_text_element(self, element):
        return element.get_attribute('innerHTML')

    def press_arrow_up(self, driver, loop = 1):
        for i in range(loop):
            driver.find_element_by_css_selector('body').send_keys(Keys.ARROW_UP)
            WaitAfterEach.sleep_timer_after_each_step()



