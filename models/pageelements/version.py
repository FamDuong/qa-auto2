from selenium.webdriver.support.wait import WebDriverWait

from models.pageelements.basepage_elements import BasePageElement
from selenium.webdriver.support import expected_conditions as ec


class VersionPageElements(BasePageElement):

    def find_element(self, driver, element):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(element))
