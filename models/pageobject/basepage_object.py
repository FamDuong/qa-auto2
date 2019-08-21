from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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


