from selenium.webdriver.support.wait import WebDriverWait


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
